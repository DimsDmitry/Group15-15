from time import sleep

class Hero():
    #конструктор класса
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health #число
        self.armor = armor #строка
    #печать параметров персонажа
    def print_info(self):
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor, '\n')

#далее запрограммируй классы-наследники суперкласса Hero

class Warrior(Hero):
    def hello(self):
        print('-> НОВЫЙ ГЕРОЙ! \nВерхом на коне появился бравый воин по имени', self.name)
        self.print_info()
        sleep(4)

    def attack(self, enemy):
        print(f'Удар! Храбрый воин {self.name} атакует {enemy.name} мечом!')
        enemy.armor -= 15
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(f'Страшный удар обрушился на противника.\nКласс брони упал до {enemy.armor}, а уровень здоровья до {enemy.health}\n')
        sleep(5)


class Magician(Hero):
    def hello(self):
        print('-> НОВЫЙ ГЕРОЙ! \nОткуда ни возьмись появился искусный волшебник', self.name)
        self.print_info()
        sleep(4)

    def attack(self, enemy):
        print(f'Удар! Ловкий маг {self.name} накладывает заклинание на {enemy.name}')
        enemy.armor -= 35
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(f'Страшное заклятье оглушило противника.\nКласс брони упал до {enemy.armor}, а уровень здоровья до {enemy.health}\n')
        sleep(5)

knight = Warrior('Henry', 100, 50)
wizard = Magician('Luke', 50, 20)

knight.attack(wizard)
wizard.attack(knight)

