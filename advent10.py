if __name__ == '__main__':
    nodes = {}
    with open('advent10.in', 'r') as f:
        for line in f.readlines():
            instruction = line.split()
            if instruction[0] == 'value':
                robot = ' '.join(instruction[-2:])
                if robot not in nodes:
                    nodes[robot] = {}
                nodes[robot]['has'] = [int(instruction[1])]
            else:
                robot = ' '.join(instruction[:2])
                if robot not in nodes:
                    nodes[robot] = {}
                nodes[robot]['low'] = ' '.join(instruction[5:7])
                nodes[robot]['high'] = ' '.join(instruction[-2:])

    keep_going = True
    while keep_going:
        for node, data in nodes.items():
            if len(data.get('has', [])) == 2:
                pass
