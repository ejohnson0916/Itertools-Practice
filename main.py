import itertools
import unittest
from unittest import TestCase

# import operator
#
# # Use count to index my data
my_data = [100, 200, 300, 400, 500, 600]
#
# my_data = list(zip(my_data, itertools.count()))
#
# print(my_data)
#
# Use Cycle to cycle through values of collection

cycle_data = itertools.cycle(my_data)


# print(next(cycle_data))
# print(next(cycle_data))
# print(next(cycle_data))
# print(next(cycle_data))
# print(next(cycle_data))
# print(next(cycle_data))
# print(next(cycle_data))
#
# Use repeat to iterate through range and get power of 2 of each num in range
# Easier to use than for loops


def repeater(my_range, my_pow):
    return list(map(pow, range(my_range), itertools.repeat(my_pow)))


# Unit Testing
class MyTest(TestCase):
    def test(self):
        self.assertEqual(repeater(10, 2), [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
        self.assertIsInstance(repeater(10, 2), list)


if __name__ == '__main__':

    my_string = 'Hello World!'
    my_list = [1, 2, 3, 4, 5]
    my_tuple = ('Hello', 'Python', 'Programmers')
    my_int = 9

    if my_int == 10:
        print(True)
    else:
        raise Exception('This is not 10')


