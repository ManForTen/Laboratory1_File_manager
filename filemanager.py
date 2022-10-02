import os # Для создания папки
import shutil # Для копирования файлов и папок

def create_file(name, text=None):
    with open(name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)

def delete_file(name):
    if os.path.isdir(name): # Если это папка удаляем её
        os.rmdir(name)
    else: # Иначе удаляем файл
        os.remove(name)

def copy_file(name, new_name):
    if os.path.isdir(name): # Если это папка, то копируем её
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Даная папка уже существует!')
    else: # Иначе копируем файл
        shutil.copy(name, new_name)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Даная папка уже существует!')

def get_list(folders_only = False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)

if __name__ == '__main__':
    create_file('test1.txt')
    create_file('test2.txt', 'Hello world!')
    create_folder('new_f')
    create_folder('new_f1')
    get_list()
    get_list(True) # Только папки
    delete_file('new_f')
    delete_file('test1.txt')
    copy_file('new_f1','new_f2')
    create_file('test3.txt','How are you?')
    copy_file('test3.txt', 'test4.txt')