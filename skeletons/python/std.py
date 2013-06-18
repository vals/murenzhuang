""" MRZ Main Module
"""


def copy(x_i):
    raise NotImplemented


def decrease_char(x_i):
    decrease_map = {"a": "z", "b": "a", "c": "b", "d": "c", "e": "d", "f": "e",
    "g": "f", "h": "g", "i": "h", "j": "i", "k": "j", "l": "k", "m": "l", "n":
    "m", "o": "n", "p": "o", "q": "p", "r": "q", "s": "r", "t": "s", "u": "t",
    "v": "u", "w": "v", "x": "w", "y": "x", "z": "y"}
    return decrease_map[x_i]


def decrease(x_i):
    try:
        x_i = int(x_i)
        return x_i - 1 % 10
    except ValueError:
        return decrease_char(x_i)


class Mutator(object):
    def __init__(self, buffer_size, transform, transform_idx, target):
        self.buffer_size = buffer_size
        self.buffer = []

        self.transform = transform
        self.transform_idx = transform_idx

        self.target = target

    def input(self, x):
        self.buffer.append(x)
        if len(self.buffer) == self.buffer_size:
            for i in self.transform_idx:
                self.target.input(self.transform(self.buffer[i - 1]))
            self.buffer = []

    def done(self):
        self.target.done()


class Printer(object):
    def __init__(self):
        self.output = []

    def input(self, x):
        self.output.append(x)

    def done(self):
        print ''.join(self.output)
        self.output = []


class FilePrinter(Printer):
    def __init__(self, file_name):
        super(FilePrinter, self).__init__()
        self.file_name = file_name

    def done(self):
        with open(self.file_name, 'w') as fh:
            fh.write(''.join(self.output))


def input(inp_str, case=0):
    printer = Printer()
    cases = [printer]
    cases.append(Mutator(3, decrease, [2], printer))
    cases.append(Mutator(3, decrease, [2], FilePrinter('file_11')))
    cases.append(Mutator(4, copy, [1], printer))
    for x in inp_str:
        cases[case].input(x)

    cases[case].done()
