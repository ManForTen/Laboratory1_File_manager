import os # Для создания папки
import shutil # Для копирования файлов и папок

def create_file(name, text=None):
    with open(name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)

def delete_file(name):
    try:
        if os.path.isdir(name): # Если это папка удаляем её
            os.rmdir(name)
        else: # Иначе удаляем файл
            os.remove(name)
    except FileNotFoundError:
        print('Данного файла не существует!')

def copy_file(name, new_name):
    if os.path.isdir(name): # Если это папка, то копируем её
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Данная папка уже существует!')
    else: # Иначе копируем файл
        shutil.copy(name, new_name)

def rename_file(name,new_name):
    os.rename(name,new_name)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Данная папка уже существует!')

def get_list(folders_only = False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)

def replace_file(name,new_name):
    os.replace(name,new_name)

def what_directory():
    print("Сейчас вы находитесь в данной директории:")
    print(os.path.abspath(os.curdir))

def go_up_directory():
    os.chdir("..")
    what_directory()

def go_to_another_directory(name):
    os.chdir(name)
    what_directory()
