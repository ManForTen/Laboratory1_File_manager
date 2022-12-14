from functions import create_file, delete_file, replace_file,copy_file, create_folder, get_list, rename_file, go_up_directory, what_directory, go_to_another_directory

print('''Действия:
---------------------------------------------------------------------------------------------------------
1. Создание папки (с указанием имени);
2. Удаление папки по имени;
3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
4. Создание пустых файлов с указанием имени;
5. Запись текста в файл;
6. Просмотр содержимого текстового файла;
7. Удаление файлов по имени;
8. Копирование файлов из одной папки в другую;
9. Перемещение файлов;
10. Переименование файлов.
11. Завершение работы файлового менеджера.
---------------------------------------------------------------------------------------------------------
''')

while True:

    try:
        A = int(input('Введите цифру:'))
    except ValueError:
        A = 0
        print('Вводите только цифры доступных действий!')

    if A == 1:
        N = input('Введите название папки:')
        create_folder(N)
        print('Папки, которые сейчас находятся в этом пути:')
        get_list(True)
    elif A == 2:
        N = input('Введите название папки, которую хотите удалить:')
        delete_file(N)
        print('Папки, которые сейчас находятся в этом пути:')
        get_list(True)
    elif A == 3:
        what_directory()
        print('''
        Выберите желаемые действия:
        ----------------------------------------
        |1. Переход в папку по имени.          |
        |2. Выход на уровень вверх в директории|
        ----------------------------------------
        ''')
        N = int(input("Введите действие:"))
        if N == 1:
            print('Доступные папки:')
            get_list(True)
            A2 = input('Введите название папки:')
            go_to_another_directory(A2)
        if N == 2:
            go_up_directory()
    elif A == 4:
        N = input('Введите название файла, который вы хотите создать:')
        create_file(N)
        print('Файлы и папки, которые сейчас находятся в этом пути:')
        get_list()
    elif A == 5:
        N1 = input('Введите название файла, в который вы хотите записать текст:')
        text_file = open(N1, "w")
        N2 = input('Введите текст:')
        text_file.write(N2)
    elif A == 6:
        N1 = input('Введите название файла, который вы хотите посмотреть:')
        text_file = open(N1, "r")
        print(text_file.read())
    elif A == 7:
        N = input('Введите название файла, который вы хотите удалить:')
        delete_file(N)
        print('Файлы и папки, которые сейчас находятся в этом пути:')
        get_list()
    elif A == 8:
        N1 = input('Введите название файла, который хотите скопировать в папку:')
        N2 = input('Введите новое название для скопированного файла:')
        copy_file(N1,N2)
        N3 = input('Введите путь и название скопированного файла(например folder/text.txt):')
        replace_file(N2, N3)
        print('Файлы и папки, которые сейчас находятся в этом пути:')
        get_list()
    elif A == 9:
        N1 = input('Введите название файла, который хотите переместить в папку:')
        N2 = input('Введите путь и название файла(например folder/text.txt):')
        replace_file(N1,N2)
        print('Файлы и папки, которые сейчас находятся в этом пути:')
        get_list()
    elif A == 10:
        N1 = input('Введите название файла, который хотите переименовать:')
        N2 = input('Введите новое название для файла:')
        rename_file(N1,N2)
        print('Файлы и папки, которые сейчас находятся в этом пути:')
        get_list()
    elif A == 11:
        break