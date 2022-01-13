#tradicional
def gcd(m, n):
    if n == 0:
        return m
    while True:
        d = int(m/n)
        x = m
        m = n
        n = x - d*m
        if (m%n == 0):
            return n

#recursiva
def gcd_rec(m,n):
    if m == 0:
        return n
    return gcd_rec(n%m, m)

#extended
#def ext(m,n):
    #mx + ny = gcd(m,n)

print(gcd(24,18))
print(gcd_rec(24,18))

print(gcd(123,36))
print(gcd_rec(123,36))

print(gcd(348,156))
print(gcd_rec(348,156))
