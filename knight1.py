from time import sleep
from random import randint

class Hero():
    #конструктор класса
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
    # печать инфо о перосонаже

    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon, '\n')

    # нанесение удара
    def strike(self, enemy):
        attack = randint(self.power-5, self.power+5)
        print(f'Удар! {self.name} атакует {enemy.name}')
        print(f'с силой {attack}, используя {self.weapon}')
        enemy.armor -= attack
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(f'{enemy.name} покачнулся(-ась).\nКласс брони упал до {enemy.armor}, а уровень здоровья до {enemy.health}\n')

    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом тяжёлом бою!\n')
                break
            sleep(3)
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в этом тяжёлом бою!\n')
                break
            sleep(3)


knight = Hero('Ричард', 50, 25, 20, 'Меч')
dragon = Hero('Дракон', 100, 25, 10, 'Пламя')

print('Средиземье в опасности! На помощь спешит доблестный рыцарь...')
knight.print_info()

sleep(5)
print(knight.name, 'идёт по лесу. Вдруг видит на пути мелкого воришку...')
sleep(5)

rascal = Hero('Питер', 20, 5, 5, 'нож')
rascal.print_info()

sleep(5)
if input('Сразиться? (да/нет)') == 'да':
    print('\nДа начнётся битва!\n')
    sleep(5)
    knight.fight(rascal)
    sleep(5)

    if knight.health > 0:
        knight.health = 50
        knight.power *= 2
        knight.armor *= 2
        print(f'\n{knight.name} восстановил силы и стал опытнее. Теперь сила его удара:{knight.power}, а класс брони:{knight.armor}\n')

sleep(5)
print(f'\nНаконец-то {knight.name} добрался до подземелья!')
dragon.print_info()
print('\nДа начнётся битва!\n')
sleep(3)
knight.fight(dragon)