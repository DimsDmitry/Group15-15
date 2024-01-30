from sport_rules import *


print('Сегодня в программе:\n1-футбол\n2-хоккей\n3-бег на 100 м')
answer = input('Ваш выбор (off - завершить):')
while answer != 'off':
    if answer == '1':
        print_football()
    elif answer == '2':
        print_hockey()
    elif answer == '3':
        print_sprint()
    else:
        print('Данный вид спорта не найден!')
    answer = input('Ваш выбор (off - завершить):')



