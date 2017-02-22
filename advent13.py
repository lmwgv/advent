def is_open(x, y):
    return not bool(bin(x * x + 3 * x + 2 * x * y + y + y * y + 1362).count("1") % 2)


def search(x, y, route):
    if not is_open(x, y):
        return False
    if x < 0 or y < 0:
        return False
    if x == 31 and y == 39:
        return True
    if (x, y) in route:
        return False
    route.append((x, y))
    if search(x, y + 1, route) or search(x + 1, y, route) or search(x - 1, y, route) or search(x, y - 1, route):
        return True
    route.pop()
    return False

if __name__ == '__main__':
    route = []
    search(1, 1, route)
    # Not the shortest, print and verify manually
    print(str(route), len(route))
    for y in range(50):
        print(''.join((('0' if (x, y) in route else '.') if is_open(x, y) else '+' for x in range(50))))
    answer2 = 0
    for y in range(51):
        for x in range(51):
            if x + y <= 50 and is_open(x, y):
                answer2 += 1
    print(answer2)
