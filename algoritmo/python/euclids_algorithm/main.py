def gcd(m, n):
    while True:
        d = int(m/n)
        x = m
        m = n
        n = x - d*m
        if (m%n == 0):
            return n

print(gcd(30,12))
print(gcd(123,36))
print(gcd(348,156))
