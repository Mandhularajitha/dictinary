dic = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':180}
first_max=0
second_max=0
third_max=0
list1=[]
for i in dic:  
    for j in dic:
        if dic[j]>first_max:
            first_max=dic[j]
            max1_key=j
        elif first_max>dic[j] and second_max<dic[j]:
            second_max=dic[i]
            second_key=j
        elif second_max >dic[j] and third_max<dic[j]:  
            third_max=dic[j]
            third_key=j
list1.append(max1_key)
list1.append(second_key)
list1.append(third_key)
print("first_max",max1_key)
print("second_max",second_key)
print("third_max",third_key)
print(list1)
