def gcd(m, n):
    while n:
        r =m % n
        m = n
        n = r
    return m

d = gcd(20,15)
print(d)
