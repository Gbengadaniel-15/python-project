file_name = input("Enter file  name : ")
if len(file_name) < 1:
    file_name = "mbox-short.txt"
    
fh = open(file_name)

dic = dict()
lst =list()

for line in fh:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    
    words = line.split()
    if len(words)<7:
        continue
    hr = words[5].split(":")
    dic[hr[0]]= dic.get(hr[0] , 0) +1
    
for k,v in dic.items():
    lst.append((k,v))
    
    
lst.sort()
for k , v in lst:
    print(k,v)


    
    
            
    
    
    
    