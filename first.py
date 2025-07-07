# Пишем и подключаем свои модули
import lib
# from lib import diff
# from . lib import summ  - из текущей директории
# from .. lib import summ  - из директории уровнем выше
# from .lib import summ  - относительный импорт (текущего файла)
print(lib.diff(7, 3))

if __name__ == '__main__':
    print(lib.summ(6, 4))

def main():
    print(lib.summ(5, 2))

if __name__ == '__main__':
    main()

from package1.module import greet       # from package1 import greet   -  когда записана упрощённый импорт
from package1 import add
print(greet('Mir!'))
print(add(3, 8))