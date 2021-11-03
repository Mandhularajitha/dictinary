dic= {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    } 
list1=[] 
max1=0
max2=0
max3=0
for k in dic:
    if dic[k]>max1:
        max2=max1
        max1=dic[k]
    elif dic[k]>max2:
        max2=dic[k]
    elif dic[k]>max3:
        max3=max2
list1.append(max1)
list1.append(max2)
list1.append(max3)
# print(max1)
# print(max2)
# print(max3) 
print(list1)