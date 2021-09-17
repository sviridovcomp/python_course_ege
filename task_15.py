def div(n, m):
    return n % m == 0

a = 1
while True:
    found = False
    for x in range(16 * 16 * 24):
        if not ((div(x, a) and div(x, 16)) <= (not (div(x, 16)) or div(x, 24))):
            found = True
            break

    if not found:
        print(a)
        break

    a += 1