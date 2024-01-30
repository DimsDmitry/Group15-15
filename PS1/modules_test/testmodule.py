from sport_salary import *


surname = input('Фамилия тренера:')
job = input('Занятость (1-полная, 2-почасовая)')
if job == '1':
    experience = int(input('Стаж в годах:'))
    salary = get_full_time(experience)
elif job == '2':
    hours = int(input(''))
    salary = get_part_time(hours)

print(surname, '-', salary)