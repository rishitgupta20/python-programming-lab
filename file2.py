word=input("Enter word to be searched:")
k = 0
 
with open('sample.txt', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                k=k+1
print("Occurrences of the word:")
print(k)	