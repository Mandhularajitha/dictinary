dic = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
b=[]
for i,j in dic.items():
    print(i,end="")
    b.append(j)
print()
i=0
while i<len(b):
    j=0
    while j<len(b):
        print(b[j][i],end=" ")
        j+=1
    print()
    i=i+1        

 


           