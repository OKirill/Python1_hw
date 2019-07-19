import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _damage_taken(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage*random.uniform(0.1, 1.0))
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage*random.uniform(0.1, 1.0))
            if self.health <= 0:
                self.health = 0

        print(f'{self.name} took damage and now has {self.health} health, {self.armor} armor'.format(self.name, self.health, self.armor))

    def punch(self, person):
        person._damage_taken(self.damage)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Fight:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def start(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.punch(person2)
            if person2.health == 0:
                print(f'********************** {person1.name} won!!')
                break
            person2.punch(person1)
            if person1.health == 0:
                print(f'********************** {person2.name} won!!')


player = Player('Player1', 200, 50, 50)
enemy = Enemy('Player2', 200, 50, 50)

new_fight = Fight(player, enemy)
new_fight.start(player, enemy)