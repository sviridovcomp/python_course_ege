expr = 9 ** 17 + 3 ** 16 - 27
result = ""
while expr:
    result += str(expr % 3)
    expr //= 3

# print(result) визуально нашёл самое часто встречающееся число
print(result.count("0"))