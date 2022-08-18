import os

from script.hi import say_hi

if __name__ == '__main__':
    say_hi(os.environ.get('NAME'))
