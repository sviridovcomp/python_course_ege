string = "1" * 2019 + "3" * 2019

while "111" in string:
    string = string.replace("111", "2", 1)
    string = string.replace("222", "3", 1)
    string = string.replace("333", "1", 1)

print(string)