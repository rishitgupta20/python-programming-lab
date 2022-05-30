with open("file.txt", "r") as f:
    largest = ""
for i in f.readlines():
        word = i.split()
        word.sort(key=len)
        if len(word[-1]) > len(largest):
            largest = word[-1]

        print(largest)