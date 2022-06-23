from itertools import count

fname = input("Enter file name")
if len(fname) < 1:
    fname = "mbox-short.txt"
name = open(fname)
words = list()

dic=dict()

for lines in name:
    line = lines.rstrip()
    if not line.startswith("From"):
        continue

    word = line.split()
    if len(word)> 3:
        continue
    words.append(word[1])

for wrd in words:
    dic[wrd]=dic.get(wrd,0) +1
#print(dic)

mostprolific = None
counts=-1

for key,value in dic.items():
    if value > counts:
        counts = value
        mostprolific= key
        
    
print (mostprolific , counts)
        
        


    
    
        