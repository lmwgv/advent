import string
from collections import Counter

if __name__ == '__main__':
    sum_of_sector_ids = 0
    ascii_lowercase = list(string.ascii_lowercase)
    with open('advent04.in', 'r') as f:
        for line in f.readlines():
            line_groups = line.split('-')
            letters = ''
            for group in line_groups[:-1]:
                letters += group
            sector_id, checksum = line_groups[-1].split('[')
            sector_id = int(sector_id)
            checksum = checksum[:-2]
            real_checksum = ''.join([x[0] for x in sorted(Counter(letters).items(), key=lambda c: '%03d-%s' % (1000 - c[1], c[0]))][:5])
            if real_checksum == checksum:
                sum_of_sector_ids += sector_id
                cypher = {c: ascii_lowercase[(n + sector_id) % len(ascii_lowercase)] for n, c in enumerate(ascii_lowercase)}
                decoded_groups = []
                for group in line_groups[:-1]:
                    decoded_groups.append(''.join((cypher[x] for x in group)))
                print(str(sector_id) + ': ' + ' '.join(decoded_groups))

    print('Sum of sector ids: %d' % sum_of_sector_ids)
