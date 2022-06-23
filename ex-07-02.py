from unicodedata import name

text = input("Enter file name:")
file_name =open(text)
count = 0
point_value =0


for line in file_name:
    
    line= line.rstrip()
    if  not line.startswith ("X-DSPAM-Confidence: ")  :
        continue
    else:
        point_value= float(point_value) + float(line [20:])
        count= count + 1
    
print("Average spam confidence: ", point_value/count )