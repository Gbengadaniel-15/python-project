file_name=input("Enter file name :")
ls=open(file_name)
print(ls)

for line in ls:
    ls= line.rstrip().upper()
    print(ls)