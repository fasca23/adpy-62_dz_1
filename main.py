from application import calculate_salary as salary
from application.db import get_employees as get
from datetime import datetime
from PIL import ImageGrab

def screen(name):
    name_ = name + '.jpg'
    pic = ImageGrab.grab()
    pic.save(f'{name_}')
    print(f'Файл {name_} создан')

if __name__ == '__main__':
    salary()
    get()
    print(str(datetime.now())[:10])
    screen('1')
