def gcd(m, n):
    n, m = min(m,n), max(m,n)
    if n == 0:
        return 0
    while m%n != 0:
        r = int(m/n)
        aux = m
        m = n
        n = aux - m*r
    return n

print(gcd(30,12))
print(gcd(60,24))
print(gcd(12,30))
print(gcd(30,0))
print(gcd(0,12))


