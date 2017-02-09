if __name__ == '__main__':
    exposed_ips = 0
    with open('advent07.in', 'r') as f:
        for line in f.readlines():
            abba_out = False
            abba_in = False
            inside_brackets = False
            for c in range(len(line) - 3):
                if line[c] == '[':
                    inside_brackets = True
                if line[c] == ']':
                    inside_brackets = False
                if line[c] == line[c + 3] and line[c + 1] == line[c + 2] and line[c] != line[c + 1]:
                    if inside_brackets:
                        abba_in = True
                    else:
                        abba_out = True
            if abba_out and not abba_in:
                exposed_ips += 1
                print(line)
    print(str(exposed_ips))
