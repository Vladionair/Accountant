import random
import unittest

class Accountant:

    def __init__(self):

        self.a = []
        self.b = []
        self.c = []
        self.n = 0
        self.m = 0
        self.sr = 0
        self.sc = 0
        self.tr = 0
        self.tc = 0
        self.value = 0

    @staticmethod

    def account(func):

        def print_res(self, n, m):

            size = 7
            self.calc(n, m)
            print()
            print(f'Введены данные, число строк: {self.n} число колонн: {self.m}')
            print()
            for i in range(self.n):
                for j in range(self.m):
                    print(str(self.a[i][j]) + ' ' * (size - len(str(self.a[i][j]))), end=' ')
                print()
            print()
            print('Проверьте правильность заполнения таблицы!')
            print()
            if self.tr == self.tc:
                print(f'Сумма строк: {self.tr} суммы строк: {self.b}')
                print()
                print(f'Сумма столбцов: {self.tc} суммы столбцов: {self.c}')
                print()
                print('Баланс сведен.')
                print()
            else:
                print('В расчетах ошибка!')

        return print_res

    def calc(self, n, m):

        self.n = n
        self.m = m

        def create_array():

            import random
            for i in range(n):
                self.a.append([])
                for j in range(m):
                    self.value = random.randint(-100, 100)
                    self.a[i].append(self.value)

        def sum_row():

            for i in range(n):
                for j in range(m):
                    self.sr += self.a[i][j]
                    self.tr += self.a[i][j]
                self.b.append(self.sr)
                self.sr = 0

        def sum_col():

            for i in range(m):
                for j in range(n):
                    self.sc += self.a[j][i]
                    self.tc += self.a[j][i]
                self.c.append(self.sc)
                self.sc = 0

        create_array()
        sum_row()
        sum_col()

check = Accountant()
count = Accountant.account(Accountant.calc)

#count(check, int(input('Введите значение n:')), int(input('Введите значение m:')))
#check.calc(int(input('Введите значение n:')), int(input('Введите значение m:')))

class Test_Accountant(unittest.TestCase):

    def test_random(self):

        Accountant.account(Accountant.calc(check, random.randint(0, 10), random.randint(0, 10)))
        self.assertEqual(Accountant().tr, Accountant().tc)

    def test_zero(self):

        Accountant.account(Accountant.calc(check, 0, 0))
        self.assertEqual(Accountant().tr, Accountant().tc)

    def test_max(self):

        Accountant.account(Accountant.calc(check, 10, 10))
        self.assertEqual(Accountant().tr, Accountant().tc)

    def test_regr(self):

        Accountant.account(Accountant.calc(check, 5, 5))
        self.assertEqual(Accountant().tr, Accountant().tc)

    def tearDownClass():

        Accountant.account(Accountant.calc(check, 0, 0))

if __name__ == '__main__':

    unittest.main(verbosity=2)