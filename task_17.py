buffer = []
for i in range(1012, 9639):
    if i % 3 ==0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i %19 !=0:
        buffer.append(i)

print(len(buffer), max(buffer))