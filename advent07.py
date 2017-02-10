if __name__ == '__main__':
    ips_supporting_tls = 0
    ips_supporting_ssl = 0
    with open('advent07.in', 'r') as f:
        for line in f.readlines():
            abas_in = []
            abas_out = []
            abba_out = False
            abba_in = False
            inside_brackets = False
            for c in range(len(line) - 2):
                if line[c] == '[':
                    inside_brackets = True
                if line[c] == ']':
                    inside_brackets = False
                if c + 3 < len(line) and line[c] == line[c + 3] and line[c + 1] == line[c + 2] and line[c] != line[c + 1]:
                    if inside_brackets:
                        abba_in = True
                    else:
                        abba_out = True
                if line[c] == line[c + 2] and line[c] != line[c + 1]:
                    if inside_brackets:
                        abas_in.append((line[c], line[c + 1]))
                    else:
                        abas_out.append((line[c + 1], line[c]))
            for aba in abas_in:
                if aba in abas_out:
                    ips_supporting_ssl += 1
                    print(str(aba) + ' ' + line[:-1])
                    break
            if abba_out and not abba_in:
                ips_supporting_tls += 1
    print(str(ips_supporting_tls))
    print(str(ips_supporting_ssl))
