from pickle import APPEND


file_name = input("enter file name " )
file = open(file_name)
data =list()
for line in file:
    fil= line.split()
    for words in fil:
        if not words in data:
            data.append(words)

print(sorted(data))