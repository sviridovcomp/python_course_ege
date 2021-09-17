with open("24-s1.txt") as f:
    data = f.readlines()
    count = 0

    for i in data:
        if i.count("YZ") > 1:
            count += 1

    print(count)