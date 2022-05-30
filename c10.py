with open("Practice.txt") as f:
    count = 0
    for line in f.readlines():
        count += 1

    print(count)