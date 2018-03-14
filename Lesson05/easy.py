# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os


def create_dirs():
    """Создает дитектории dir_1 - dir_9 в папке"""
    for i in range(1, 10):
        directory = 'dir_{}'.format(i)
        create_dir(directory)


def create_dir(directory):
    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
            return True
        except PermissionError:
            print('Отказано в доступе')
    return False


def delete_dirs():
    """Удаляет директории dir_1 - dir_9"""
    for i in range(1, 10):
        delete_dir('dir_{}'.format(i))

def delete_dir(directory):
    try:
        os.rmdir(directory)
        return True
    except PermissionError:
        print('Отказано в доступе')
    except FileNotFoundError:
        print('Не найдена директория dir_{}'.format(directory))
    except OSError:
        print('Папка не пуста dir_{}'.format(directory))
    return False


if __name__ == '__main__':
    create_dirs()
    delete_dirs()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_dirs():
    """Отображает папки текущей директории."""
    for dir in os.listdir(os.getcwd()):
        if os.path.isdir(dir):
            print(dir)


if __name__ == '__main__':
    show_dirs()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():
    """Создает копию файла, из которого запущен"""
    with open(__file__, encoding='UTF-8') as f:
        with open('copy_' + os.path.basename(__file__), 'w', encoding='UTF-8') as w:
            w.writelines(f.readlines())


def delete_copyes():
    """Удаляет созданные копии функцией copy_current_file"""
    files_to_del = [d for d in os.listdir(os.getcwd()) if os.path.isfile(d) and d.startswith('copy_')]
    os.remove(*files_to_del)


if __name__ == '__main__':
    copy_current_file()
    delete_copyes()

# Для задания normal

def directory_action(action, ok ='успешно', failure = 'Ошибка', log = None):
    '''Действия над директорией - для задания normal'''
    directory = input('введите назнвание директории')
    path = os.path.join(os.getcwd(), directory)
    if action(path):
        print(ok)
        if log != None: log(path)
    else:
        print(failure)

def change_directory():
    directory = input('введите назнвание директории')
    os.chdir(directory)
    print(f'Вы находитесь: {os.getcwd()}')

