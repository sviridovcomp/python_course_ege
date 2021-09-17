def f(x):
    X = x
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if M < (x % 10):
            M = x % 10
        x = x // 10
    return L, M


buffer = []
for i in range(10000):
    if f(i) == (3, 7):
        buffer.append(i)

print(max(buffer))
