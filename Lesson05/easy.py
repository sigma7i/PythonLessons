# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os


def create_dirs():
    for i in range(1, 10):
        directory = 'dir_{}'.format(i)
        if not os.path.exists(directory):
            try:
                os.mkdir(directory)
            except PermissionError:
                print('Отказано в доступе')


def delete_dirs():
    for i in range(1, 10):
        try:
            os.rmdir('dir_{}'.format(i))
        except PermissionError:
            print('Отказано в доступе')
        except FileNotFoundError:
            print('Не найдена директория dir_{}'.format(i))
        except OSError:
            print('Папка не пуста dir_{}'.format(i))


if __name__ == '__main__':
    create_dirs()
    delete_dirs()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_dirs():
    for dir in os.listdir(os.getcwd()):
        if os.path.isdir(dir):
            print(dir)


if __name__ == '__main__':
    show_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys


def copy_current_file():
    with open(sys.argv[0], encoding='UTF-8') as f:
        with open('copy_' + os.path.basename(sys.argv[0]), 'w', encoding='UTF-8') as w:
            w.writelines(f.readlines())


if __name__ == '__main__':
    copy_current_file()
