class Map:
    def __init__(self, size_x, size_y, empty_char=" "):
        self.size_x = size_x
        self.size_y = size_y
        self.table = []
        self.empty_char = empty_char

        for x in range(self.size_x):
            self.table.append([])
            for y in range(self.size_y):
                self.table[x].append(self.empty_char)

    def print_table(self):
        for x in range(self.size_x):
            self.table[x][0] = '|'
            self.table[x][-1] = '|'

        for y in range(self.size_y):
            self.table[0][y] = '_'
            self.table[-1][y] = '-'

        for x in range(self.size_x):
            for y in range(self.size_y):
                print(self.table[x][y], end=" ")
            print()

    def clear_table(self):
        for x in range(self.size_x):
            for y in range(self.size_y):
                self.table[x][y] = self.empty_char

    def set_value(self, x, y, char):
        self.table[x][y] = char
