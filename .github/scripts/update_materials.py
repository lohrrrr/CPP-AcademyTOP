"""Обновление материалов с сохранением существующих решений студента.

python3 update_materials.py TEMPLATE_DIRECTORY STUDENT_DIRECTORY
Обновляет материалы преподавателя, добавляет недостающие заготовки.
Существующие решения и отчёты, личный README и .github сохраняются.
"""

from pathlib import Path
import os
import shutil
import sys


TEACHER_DIRS = {"docs", "lectures", "materials", "assets"}
WORK_DIRS = {"practice", "homework", "exams"}
TEACHER_FILES = {".gitignore", ".gitattributes", ".editorconfig"}


def is_teacher(path):
    parts = path.parts
    if parts[0] in TEACHER_DIRS or path.as_posix() in TEACHER_FILES:
        return True
    if parts[0] in WORK_DIRS:
        return ((len(parts) == 2 and parts[1] == "README.md")
                or (len(parts) == 3 and parts[2] in {"README.md", "tasks.md"}))
    return False


def allowed(path):
    return (path.parts[0] in TEACHER_DIRS | WORK_DIRS
            or path.as_posix() in TEACHER_FILES)


def sync_materials(template, student):
    template, student = Path(template).resolve(), Path(student).resolve()
    if template == student or template in student.parents or student in template.parents:
        raise ValueError("Папки шаблона и студента должны быть отдельными.")
    changes = []
    for source in sorted(template.rglob("*")):
        relative = source.relative_to(template)
        if not allowed(relative) or source.is_symlink() or not source.is_file():
            continue
        if any(parent.is_symlink() for parent in source.parents if parent != template):
            continue
        target = student / relative
        if target.is_symlink() or any(parent.is_symlink() for parent in target.parents if parent != student):
            continue
        # Проверка пути сохраняет перенос внутри репозитория студента.
        if student not in target.resolve().parents:
            continue
        if target.exists():
            if not is_teacher(relative) or not target.is_file():
                continue
            if source.read_bytes() == target.read_bytes():
                continue
            action = "обновлён"
        else:
            action = "добавлен"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        changes.append(f"- {action}: `{relative.as_posix()}`")
    return changes


def main():
    if len(sys.argv) != 3:
        sys.exit("Запуск: python3 update_materials.py TEMPLATE_DIRECTORY STUDENT_DIRECTORY")
    lines = sync_materials(sys.argv[1], sys.argv[2])
    report = "\n".join(lines) if lines else "Новых материалов нет."
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as stream:
            stream.write("## Обновление материалов курса\n\n" + report + "\n")


if __name__ == "__main__":
    main()
