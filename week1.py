import numpy as np


class Car:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def seat(self):
        if self.n1 < 5:
            print("Allotted seat in car 1")

        elif 5 <= self.n1 + self.n2 < 10:
            print("Allotted seat in car 2")

        else:
            print("There is no seat in the cars")


class Bus:
    def __init__(self, m):
        self.m = m

    def seat(self):
        if self.m < 25:
            print("Allotted sitting space in the bus")

        elif 25 <= self.m < 40:
            print("Allotted standing space in the bus")

        else:
            print("There is no space in the bus")


n1 = 0
n2 = 0
m = 0

while True:
    a = input("Enter A if u want car and B if u want bus and C if u want to remove a person")
    if a == 'A':
        x = Car(n1, n2)
        x.seat()
        if n1 < 5:
            n1 += 1
        elif n1 == 5 and n2 < 5:
            n1 += 0
            n2 += 1
        elif n1 == 5 and n2 == 5:
            n1 += 0
            n2 += 0
        print(f'number of empty spaces in car 1={5-n1}')
        print(f'number of empty spaces in car 2={5-n2}')
        print(f'number of empty spaces in bus={40-m}')

    elif a == 'B':
        x = Bus(m)
        x.seat()
        if m < 40:
            m += 1
        elif m == 40:
            m += 0
        print(f'number of empty spaces in car 1={5-n1}')
        print(f'number of empty spaces in car 2={5-n2}')
        print(f'number of empty spaces in bus={40-m}')
    elif a == 'C':
        x = np.random.rand()
        if x < 0.6:
            if 0 < m <= 25:
                print("Remove a sitting person from bus")
                m = m - 1
            elif 25 < m <= 40:
                print("Remove a standing person from bus")
                m = m - 1
            else:
                print("You cannot remove a person from bus")
        elif x < 0.8:
            if 0 < n1 <= 5:
                print("Remove a person from car 1")
                n1 = n1 - 1
            else:
                print("You cannot remove a person from car 1")
        else:
            if n2 != 0:
                print("Remove a person from car 2")
                n2 = n2 - 1
            else:
                print("You cannot remove a person from car 2")
        print(f'number of empty spaces in car 1={5 - n1}')
        print(f'number of empty spaces in car 2={5 - n2}')
        print(f'number of empty spaces in bus={40 - m}')
    else:
      break