import hashlib

if __name__ == '__main__':
    seed = b'ugkcyxxp'
    password = ''
    password2 = list('        ')
    n = 0

    while len(password) < 8 or ' ' in password2:
        candidate = seed + bytes(str(n).encode('ascii'))
        hash = str(hashlib.md5(candidate).hexdigest())
        if hash.startswith('00000'):
            if len(password) < 8:
                password += hash[5]
                print('Char found at %d: %s' % (n, password))
            if hash[5] in '01234567' and password2[int(hash[5])] == ' ':
                password2[int(hash[5])] = hash[6]
                print('Char found at %d: %s' % (n, ''.join(password2)))
        n += 1

    print(password + ' ' + ''.join(password2))
