class Pizza:

    def __init__(self):
        self._grid = []
        self._parts = []
        self._min_ingredient = 1
        self._max_part_size = 6
        self.filename = ''

    def read(self, filename):
        self.filename = filename
        with open('../inputs/%s.in' % filename) as f:
            fl = list(map(int, f.readline().split()))
            self._min_ingredient = fl[2]
            self._max_part_size = fl[3]
            self._grid = list(map(lambda l: list(l.strip()), f))

    def slice(self, rows, cols):
        if self.is_valid_part(rows, cols):
            self._parts.append((rows, cols))
        else:
            raise ArithmeticError('invalid slice')

    def is_valid_pizza(self):
        part_sizes = sum(self.part_size(rs, cs) for rs, cs in self._parts)
        return part_sizes == self.size()

    def is_valid_part(self, rows, cols):
        num_mus = 0
        num_tom = 0
        for r in self._grid[rows[0]:rows[1] + 1]:
            for c in r[cols[0]:cols[1] + 1]:
                if c == 'T':
                    num_tom += 1
                elif c == 'M':
                    num_mus += 1
                else:
                    raise ValueError()

        return num_mus >= self._min_ingredient   \
            and  num_tom >= self._min_ingredient \
            and self._max_part_size >= self.part_size(rows, cols)

        return True

    def parse_to_file(self):
        with open('../outputs/%s.txt' % self.filename, 'w') as f:
            f.write('%s\n' % str(len(self._parts)))
            for rows, cols in self._parts:
                f.write('%s %s %s %s\n' % (rows[0], cols[0], rows[1], cols[1]))

    def size(self):
        return len(self._grid) * len(self._grid[0])

    def part_size(self, rows, cols):
        return (rows[1] - rows[0] + 1) * (cols[1] - cols[0] + 1)
