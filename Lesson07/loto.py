
import random


class LotoCard:
    def __init__(self, rows = 3, colums = 9, numbers = 5):
        self.rows = rows
        self.colums = colums
        self.numbers = numbers
        self.card = []

    def generate_card(self):
        uq_numbers = self._generate_unique_num()
        self.card = [self._generate_row(uq_numbers) for _ in range(0, self.rows)]
        print(self.card)

    def _generate_unique_num(self):
        unique_num = set()
        while len(unique_num) < self.rows * self.numbers:
            unique_num.add(random.randint(1, 90))

        return unique_num

    def _generate_row(self, uq_numbers):
        unique_row = [uq_numbers.pop() for _ in range(0, self.numbers)]
        spaces_count = self.colums - self.numbers
        spaces = [' ' for _ in range(0, spaces_count)]
        unique_row += spaces
        random.shuffle(unique_row)
        # сотритровка
        return unique_row

    def print_card(self):
        print('-' * 26)
        for r in self.card:
            row = []
            for c in r:
                if c == ' ':
                    row.append('  ')
                elif 1 < c < 10:
                    row.append(f' {c}')
                else:
                    row.append(str(c))
            print(' '.join(row))

        print('-' * 26)







card = LotoCard()
card.generate_card()
card.print_card()