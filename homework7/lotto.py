import random
import sys
import time


class Barrel:
    def __init__(self, amount):
        self.amount = amount
        self.gen = self.field()

    def field(self):
        numbers = [x for x in range(1, self.amount + 1)]
        random.shuffle(numbers)
        for i, y in enumerate(numbers):
            print('{:*^30}'.format('Игра в Лотто'))
            print(f'Текущий бочонок: {y} (осталось {self.amount - (i + 1)})')
            yield y


class Game:
    def __init__(self, amount_card):
        row = 3
        self.all_row = row * amount_card
        self.__set_card()

    def __set_card(self):
        num = set()
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        random.shuffle(cards)

        while len(cards) % self.all_row != 0:
            cards.append('None')
        self.all_row = int(len(cards) / self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]

        for i in range(len(cards)):
            cards[i].sort()
        self.card_user = cards[:3]
        self.card_comp = cards[3:]

    def get_card(self, card_player):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_player[0]))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_player[1]))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_player[2]))
        print('{:-^25}'.format('-'))

    def search(self, card_player, num_barrel):
        for i, n in enumerate(card_player):
            if num_barrel in n:
                card_player[i][n.index(num_barrel)] = '|X|'
                self.score += 1
                if self.score == 15:
                    print('{} Победил!'.format(self.name))
                    sys.exit(1)
                return True
        return False


class Player(Game):

    def __init__(self, name):
        self.name = name
        self.score = 0


def play():
    game = Game(2)
    barrel = Barrel(90)
    player1 = Player('Игрок')
    player2 = Player('Компьютер')

    while True:
        num_barrel = next(barrel.gen)
        player1.get_card(game.card_user)
        player2.get_card(game.card_comp)

        inp_user = input('Зачеркнуть цифру? (y/n)')
        if inp_user == 'y':
            if player1.search(game.card_user, num_barrel):
                continue
            else:
                print('Конец игры')
                sys.exit(1)
        if inp_user == 'n':
            if player1.search(game.card_user, num_barrel):
                print('Игра окончена')
                sys.exit(1)
            elif player2.search(game.card_comp, num_barrel):
                continue
        if inp_user != 'n' and inp_user != 'y':
            print('Введите y or n')
            time.sleep(1)
            continue


if __name__ == '__main__':
    play()