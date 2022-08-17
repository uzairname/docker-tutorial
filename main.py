import os

from script.hi import print_hi

if __name__ == '__main__':
    print_hi(os.environ.get('NAME'))
