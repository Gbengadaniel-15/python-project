file_name =input("Enter file name")
if len(file_name) < 1:
    file_name="mbox-short.txt"
file = open(file_name)
count = 0

for line in file:
    
    line=line.rstrip()
    if not line.startswith("From"):
        continue
        
    word = line.split()
    if len(word)<3:
        continue
    new =word[1]
    count =count + 1
    print(new)
print("There were", count, "lines in the file with From as the first word")
