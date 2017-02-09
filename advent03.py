def is_impossible(sides):
    impossible = False
    if sides[0] + sides[1] <= sides[2]:
        impossible = True
    if sides[1] + sides[2] <= sides[0]:
        impossible = True
    if sides[0] + sides[2] <= sides[1]:
        impossible = True
    return impossible

if __name__ == '__main__':
    num_possibles = 0
    with open('advent03.in', 'r') as f:
        for line in f.readlines():
            sides = [int(x.strip()) for x in line.split()]
            num_possibles += 1 if not is_impossible(sides) else 0
    print('Possible triangles (Horizontally): %d' % num_possibles)

    num_possibles = 0
    with open('advent03.in', 'r') as f:
        triangles = [[], [], []]
        for line in f.readlines():
            points = [int(x.strip()) for x in line.split()]
            for i in range(len(points)):
                triangles[i].append(points[i])
            if len(triangles[0]) == 3:
                for i in range(len(triangles)):
                    num_possibles += 1 if not is_impossible(triangles[i]) else 0
                triangles = [[], [], []]
    print('Possible triangles (Vertically): %d' % num_possibles)
