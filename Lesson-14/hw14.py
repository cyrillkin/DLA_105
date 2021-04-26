import unittest
from hw04_easy import *
from hw04_normal import *


class Test(unittest.TestCase):
    def test_list_int(self):
        result_1 = convert(10)
        result_2 = float(my_round(2.1234567, 4))
        result_3 = float(my_round_2('2.1234567', 5))
        result_4 = lucky_ticket(123006)
        result_5 = lucky_ticket_2(123006)
        result_6 = fibonacci(1, 10)
        result_7 = filter((lambda x: x > 5), parameter=[1, 5, 10, 2, 46])
        result_8 = paral((0, 0), (1, 1), (3, 1), (2, 0))
        self.assertEqual(result_1, 16.09)
        self.assertEqual(result_2, 2.1235)
        self.assertEqual(result_3, 2.12346)
        self.assertEqual(result_4, True)
        self.assertEqual(result_5, True)
        self.assertEqual(result_6, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(result_7, [10, 46])
        self.assertEqual(result_8, True)


if __name__ == '__main__':
    unittest.main()