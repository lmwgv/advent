'''
The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.
'''
class Receiver():
    def __init__(self):
        self.has = []

    def get(self, value):
        self.has.append(value)

    def hands_full(self):
        return False


class Bot(Receiver):
    def __init__(self):
        super().__init__()
        self.high = None
        self.low = None

    def hands_full(self):
        return len(self.has) == 2

    def give(self, nodes):
        values = sorted(self.has)
        print('Gives %d to %s, %d to %s' % (values[0], self.low, values[1], self.high))
        if values == [17, 61]:
            print("I'M THE MAN!!!!")
        nodes[self.low].get(values[0])
        nodes[self.high].get(values[1])
        self.has = []


if __name__ == '__main__':
    nodes = {}
    with open('advent10.in', 'r') as f:
        for line in f.readlines():
            instruction = line.split()
            if instruction[0] == 'value':
                robot = ' '.join(instruction[-2:])
                if robot not in nodes:
                    nodes[robot] = Bot()
                nodes[robot].get(int(instruction[1]))
            else:
                robot = ' '.join(instruction[:2])
                if robot not in nodes:
                    nodes[robot] = Bot()
                nodes[robot].low = ' '.join(instruction[5:7])
                nodes[robot].high = ' '.join(instruction[-2:])
                for attr in 'low', 'high':
                    destination = getattr(nodes[robot], attr)
                    if destination not in nodes:
                        nodes[destination] = Bot() if 'bot' in destination else Receiver()

    # Who compares 61 and 17?
    while True:
        full_nodes = [(k, v) for k, v in nodes.items() if v.hands_full()]
        if not len(full_nodes):
            break
        for node, data in [(k, v) for k, v in nodes.items() if v.hands_full()]:
            print(node)
            data.give(nodes)

    first_outputs = [nodes['output ' + str(x)].has[0] for x in range(3)]
    print(first_outputs)
    ans = 1
    for output in first_outputs:
        ans *= output
    print(ans)
