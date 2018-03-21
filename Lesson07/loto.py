import random


class LotoCard:
    def __init__(self, card_name, rows=3, card_colums=9, numbers=5):
        self._card_name = card_name
        self._rows = rows
        self._colums = card_colums
        self._numbers = numbers
        self._card = []
        self._card_numbers = set()
        self._generate_card()

    @property
    def card_name(self):
        return self._card_name

    @property
    def numbers(self):
        return list(self._card_numbers)

    def _generate_card(self):
        uq_numbers = self._generate_unique_num()
        self._card_numbers = uq_numbers.copy()
        self._card = [self._generate_row(uq_numbers) for _ in range(0, self._rows)]

    def _generate_unique_num(self):
        unique_num = set()
        while len(unique_num) < self._rows * self._numbers:
            unique_num.add(random.randint(1, 90))

        return unique_num

    def _generate_row(self, uq_numbers):
        unique_row = [uq_numbers.pop() for _ in range(0, self._numbers)]
        unique_row.sort()

        spaces_count = self._colums - self._numbers
        for _ in range(0, spaces_count):
            unique_row.insert(random.randint(0, self._numbers), ' ')

        return unique_row

    def print_card(self):
        print('   -=', self._card_name, ':=-')
        print('-' * 26)
        for r in self._card:
            row = []
            for c in r:
                if c == ' ':
                    row.append('  ')
                elif c == '-':
                    row.append('-')
                elif 1 < c < 10:
                    row.append(f' {c}')
                else:
                    row.append(str(c))
            print(' '.join(row))

        print('-' * 26)

    def crossout_number(self, number):
        if self.number_exists(number):
            for r in self._card:
                for index, value in enumerate(r):
                    if value not in (' ', '-') and value == number:
                        r[index] = '-'
                        self._card_numbers.remove(number)
                        return True

        return False

    def number_exists(self, number):
        return number in self.numbers

    def check_for_win(self):
        return len(self._card_numbers) == 0


class LotoGame:
    def __init__(self, player, computer, auto_game=False, random_choice=False):
        self._kegs_total_count = 90
        self._kegs = []
        self._generate_kegs()
        self._player = player
        self._computer = computer
        self._auto_game = auto_game
        self._israndom_choice = random_choice

    def _generate_kegs(self):
        self._kegs = [n for n in range(1, self._kegs_total_count + 1)]
        self.shuffle_kegs()

    def shuffle_kegs(self):
        random.shuffle(self._kegs)
        print('перемешеиваю мешочек с бочонками...')

    def show_cards(self):
        for c in (self._player, self._computer):
            c.print_card()

    def _player_interface(self, keg):

        if self._auto_game:
            return self._player_autogame(keg)

        answer = input('Зачеркнуть цифру? (y/n)')
        if answer == 'y':
            result = self._player.crossout_number(keg)
            if not result:
                print('цифры на карточке нет, компьютер выйграл')
                return False
        elif answer == 'n':
            result = self._player.crossout_number(keg)
            if result:
                print('цифры на карточке нет, компьютер выйграл')
                return False
        else:
            print('необходимо корректно выбрать действие')
        return True

    def _player_autogame(self, keg):
        if self._player.number_exists(keg):
            result = self._player.crossout_number(keg)
            if not result or self._random_choice():
                print('цифры на карточке нет, компьютер выйграл')
                return False
        else:
            result = self._player.crossout_number(keg)
            if result or self._random_choice():
                print('цифра есть на карточке, компьютер выйграл')
                return False

        return True

    def _random_choice(self):
        """эмулирует случайный выбор игрока"""
        if not self._israndom_choice:
            return False

        rand_check = random.randint(0, 150)
        rendom_number = random.randint(0, 80)
        return rand_check == rendom_number

    def _computer_game(self, keg):
        self._computer.crossout_number(keg)

    def _check_for_win(self):
        if self._player.check_for_win():
            self.show_cards()
            print('игрок выйграл')
            return True
        elif self._computer.check_for_win():
            self.show_cards()
            print('компьютер выйграл')
            return True
        return False

    def next_round(self):
        self.shuffle_kegs()
        keg = self._kegs.pop()
        kegs_current_count = len(self._kegs)

        print(f'Новый бочонок: {keg} (осталось {kegs_current_count})')
        self.show_cards()

        self._computer_game(keg)
        continue_game = self._player_interface(keg)
        we_have_winner = self._check_for_win()

        if not continue_game or we_have_winner:
            return False

        if kegs_current_count == 0:
            print('бочонки закончились')
            return False

        return True


if __name__ == '__main__':
    card = LotoCard('карта игрока')
    comp_card = LotoCard('карта компьютера')

    auto_game = True # авто игра без участия игрока
    random_choice = True # эмулирует случайный выбор игрока

    loto = LotoGame(card, comp_card, auto_game, random_choice)

    while loto.next_round():
        continue
