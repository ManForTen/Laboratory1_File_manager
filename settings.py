import os
def settings(path):
    os.chdir(path)
print('Для начала работы файлового менеджера, вам надо его настроить!')
A = input('Если вы хотите изменить директорию, напишите да:')
if A == 'да' or A == 'Да':
    path = input('Введите полный путь до директории:')
    settings(path)
