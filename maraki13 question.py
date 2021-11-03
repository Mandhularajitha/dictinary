dic = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':180}
max=0
sec=0
third=0
for i in dic:
    for j in dic:
        if dic[i]>max:
            max=dic[i]
            temp1=i
        elif max>dic[j] and sec<dic[j]:
            sec=dic[j]
            temp2=j
        elif sec>dic[j] and third<dic[j]:
            third=dic[i]
            temp3=i
            
print(max,temp1)
print(sec,temp2)
print(third,temp3)

        