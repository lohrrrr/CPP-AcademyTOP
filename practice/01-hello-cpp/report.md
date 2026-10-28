# Отчёт по практике 01

| Поле | Данные |
|---|---|
| Студент | Плотников Яромир |
| Группа | 9/2-РПО-25/1 |
| Дата | Октябрь 28, 5:39 по UTC |
| Среда и компилятор | Linux, VsCode, clang, g++ |

## Что выполнено

- [X] Стартовая программа запущена
- [X] Добавлена карточка в консоли
- [X] Изучено и исправлено сообщение об ошибке
- [X] Изменения отправлены на GitHub

## Как запустить

```sh
/usr/bin/g++ -fdiagnostics-color=always -g /home/lohrrrr/Desktop/College/CPP-AcademyTOP/practice/01-hello-cpp/main.cpp -o /home/lohrrrr/Desktop/College/CPP-AcademyTOP/practice/01-hello-cpp/main
chmod +x main
./main
```

## Вывод программы

```text
macbook% ./practice/01-hello-cpp/main 
Hello, C++!
RPO 1
2y kurs
```

## Разбор ошибки

Компилятор выдал ошибку
```text
/home/lohrrrr/Desktop/College/CPP-AcademyTOP/practice/01-hello-cpp/main.cpp: In function ‘int main()’:
/home/lohrrrr/Desktop/College/CPP-AcademyTOP/practice/01-hello-cpp/main.cpp:6:36: error: expected ‘;’ before ‘return’
    6 |     std::cout << "RPO 1\n2y kurs\n"
      |                                    ^
      |                                    ;
    7 |
    8 |     return 0;
      |     ~~~~~~

Build finished with error(s).
```

Сама ошибка явно указывает что нет ;, а ; нужна ибо в случае с C++ ему все равно на раздельные строки, он разделяет комманды как раз таки ;.

## Ответы на вопросы

1. Начало выполнения программы: программа начинает выполняться с main, сам main должен вернуть ОС четное число по завершении.
2. Назначение `std::cout`: вывод текста в терминал через библиотеку iostream
3. Назначение `\n`: перевод на новую строку без std::endl;
4. Проверка отправки на GitHub: git fetch

## Что осталось непонятным

Вопросов нет
