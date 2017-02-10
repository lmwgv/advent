def decompress(string, recursive=True):
    total_length = 0
    n = 0
    while n < len(string):
        if string[n] == '(':
            length, times = string[n + 1:].split(')')[0].split('x')
            n += len(length) + len(times) + 3
            total_length += int(times) * (decompress(string[n: n + int(length)]) if recursive else int(length))
            n += int(length)
        else:
            total_length += 1
            n += 1
    return total_length

if __name__ == '__main__':
    with open('advent09.in', 'r') as f:
        line = f.readline()

    print(decompress(line[:-1], recursive=False))
    print(decompress(line[:-1]))
