import unittest


class TestMyFunction(unittest.TestCase):
    def test_ordinary_case(self):
        input_data = {'JD': [13, 89, 32, 55],
                      'Turk': [5, 32, 57, 39],
                      'Janitor': [100, 100, 100, 100]}
        result = {"JD's rating": 47.25,
                  "Turk's rating": 33.25,
                  "Janitor's rating": 100.00}
        self.assertEqual(my_func(input_data), result)

    def test_other_data_type(self):
        input_data = [3, 'JD', True, (33, 77), ['slay', 'invoke', ]]
        for i in input_data:
            self.assertRaises(ValueError, my_func, i)

    def test_empty_list(self):
        input_data = {'Jon Snow': []}
        result = {"Jon Snow's rating": 0}
        self.assertEqual(my_func(input_data), result)