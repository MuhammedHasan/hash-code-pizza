from pizza import Pizza


class Cutter:

    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def solve(self, i, j):
        for r in range(0, self.pizza.heigth() - i, i):
            for c in range(0, self.pizza.width() - j, j):
                try:
                    self.pizza.slice((r, (r + i - 1)), (c, (c + j - 1)))
                except:
                    pass
        self.pizza.parse_to_file()
