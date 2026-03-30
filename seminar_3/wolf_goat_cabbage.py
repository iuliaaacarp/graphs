from parse import *

_list = ['G', 'W', 'C', 'B']

class WolfGoatCabbageState:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        value = 0
        for i in _list:
            if not self.data[i]:
                value += i
        value += '-'
        for i in _list:
            if self.data[i]:
                value += i
        return value

    def __eq__(self, other):
        if isinstance(other, WolfGoatCabbageState):
            return self.data == other.data
        return False

    def __ne__(self, other):
        pass

    def __hash__(self):
        pass

    def parse_neighbours(self):
        pass

class WolfGoatCabbageGraph:
    def parse_out(self, x):
        return x.parse_neighbours()

    def parse_in(self, y):
        return y.parse_neighbours()

    def initial_state(self):
        data = {'G': False, 'W': False, 'C': False, 'B': False}
        return WolfGoatCabbageState(data)

    def initial_states(self):
        data = {'G': True, 'W': True, 'C': True, 'B': True}
        return WolfGoatCabbageState(data)

if __name__ == "__main__":
    g = WolfGoatCabbageGraph()
    s = g.initial_state()
    t = g.final_state()

    path = shotest_path(g, s, t)