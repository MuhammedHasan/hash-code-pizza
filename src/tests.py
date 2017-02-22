import unittest
from pizza import Pizza


class TestPizza(unittest.TestCase):

    def setUp(self):
        self.pizza = Pizza()
        self.pizza._grid = [
            ['T', 'T', 'T', 'T', 'T'],
            ['T', 'M', 'M', 'M', 'T'],
            ['T', 'T', 'T', 'T', 'T'],
        ]
        self._min_ingredient = 1
        self._max_part_size = 0

    def test_read(self):
        pizza = Pizza()
        pizza.read('example')
        self.assertEqual(self.pizza._grid, pizza._grid)
        self.assertEqual(self.pizza._min_ingredient, pizza._min_ingredient)
        self.assertEqual(self.pizza._max_part_size, pizza._max_part_size)

    def test_slice(self):
        pass

    def test_is_valid_pizza(self):
        self.assertTrue(not self.pizza.is_valid_pizza())

        self.pizza.slice((0, 2), (0, 1))
        self.assertTrue(not self.pizza.is_valid_pizza())

        self.pizza.slice((0, 2), (2, 2))
        self.assertTrue(not self.pizza.is_valid_pizza())

        self.pizza.slice((0, 2), (3, 4))
        self.assertTrue(self.pizza.is_valid_pizza())

    def test_is_valid_part(self):
        self.assertTrue(self.pizza.is_valid_part((0, 2), (0, 1)))
        self.assertTrue(not self.pizza.is_valid_part((0, 2), (0, 4)))


if __name__ == '__main__':
    unittest.main()
