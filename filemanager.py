import os # Для создания папки

def create_file(name, text=None):
    with open(name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Даная папка уже существует!')


if __name__ == '__main__':
    create_file('test1.txt')
    create_file('test2.txt', 'Hello world!')
    create_folder('new_f')