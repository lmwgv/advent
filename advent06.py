from collections import Counter

if __name__ == '__main__':
    columns = None
    with open('advent06.in', 'r') as f:
        for line in f.readlines():
            if columns is None:
                columns = [[] for x in range(len(line))]
            for i in range(len(line)):
                columns[i].append(line[i])
    message = ''.join(Counter(x).most_common()[0][0] for x in columns)
    message2 = ''.join(Counter(x).most_common()[-1][0] for x in columns)
    print(message)
    print(message2)
