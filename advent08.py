def rotate(l, d):
    return l[-d:] + [l[x - d] for x in range(d, len(l))]

if __name__ == '__main__':
    with open('advent08.in', 'r') as f:
        screen = [[0 for x in range(50)] for y in range(6)]
        for line in f.readlines():
            command = line.split()
            if command[0] == 'rect':
                rect_width, rect_height = (int(x) for x in command[1].split('x'))
                for row in range(rect_height):
                    screen[row][:rect_width] = [1 for x in range(rect_width)]
            elif command[0] == 'rotate':
                what = int(command[2].split('=')[1])
                how_much = int(command[4])
                if command[1] == 'row':
                    screen[what] = rotate(screen[what], how_much)
                elif command[1] == 'column':
                    aux = [x[what] for x in screen]
                    aux = rotate(aux, how_much)
                    for n, row in enumerate(screen):
                        row[what] = aux[n]

    print(str(sum((sum(x) for x in screen))))
    for row in screen:
        print(''.join(('*' if x else ' ' for x in row)))
