list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
i=0
x={}
while i<len(list1):
    a=list1[i]
    x[a]=list2[i]
    i=i+1 
print(x)  
