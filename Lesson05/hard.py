# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# P.S. Внизу есть тест проверяющий всю функциональность

import os
import sys
import Lesson05.easy as easy

def print_help(_):
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')

def make_dir(directory):
    dir_path = os.path.join(os.getcwd(), directory)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(directory))
    except FileExistsError:
        print('директория {} уже существует'.format(directory))


def ping(_):
    print('pong')


def delete_file_confirm(file):
    confirm = input(f'хотите удалить файл {file}(y/n)')

    if confirm == 'y':
        path = os.path.join(os.getcwd(), file)
        os.remove(path)


def cd_to_dir(path):
    os.chdir(path)
    print(os.getcwd())

def start_programm():
    print('sys.argv = ', sys.argv)

    do = {
        'help': print_help,
        'mkdir': make_dir,
        'ping': ping,
        'cp': easy.copy_file,
        'rm': delete_file_confirm,
        'cd': cd_to_dir,
        'ls': easy.show_dirs
    }

    try:
        key = sys.argv[1]
    except IndexError:
        key = None

    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None

    if key:
        if not dir_name and key not in ('ls','help', 'ping'):
            print('Необходимо указать имя директории вторым параметром')
            return

        if do.get(key):
            do[key](dir_name)
        else:
            print('Задан неверный ключ')
            print('Укажите ключ help для получения справки')

def tests():
    sys.argv.append('')
    sys.argv.append('')

    sys.argv[1] = 'help'
    sys.argv[2] = ''
    start_programm()

    sys.argv[1] = 'mkdir'
    sys.argv[2] = 'newDir'
    start_programm()

    sys.argv[1] = 'ping'
    sys.argv[2] = ''
    start_programm()

    sys.argv[1] = 'cp'
    sys.argv[2] = 'normal.py'
    start_programm()

    sys.argv[1] = 'rm'
    sys.argv[2] = 'copy_normal.py'
    start_programm()

    sys.argv[1] = 'cd'
    sys.argv[2] = 'newDir'
    start_programm()

    sys.argv[1] = 'ls'
    sys.argv[2] = ''
    start_programm()


if __name__ == '__main__':
    tests()



