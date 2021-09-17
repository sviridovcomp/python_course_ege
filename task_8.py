from itertools import permutations

s = set()

for (a, b, c, d, e, f) in permutations("МОЛОКО", 6):
    s.add(a + b + c + e + f)

print(len(s))