# assending and decending order

dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
l=list(dic.values())

l.sort()
a=l.copy()
a.reverse()
print(l)

x={}
for i in l:
    for j in dic:
        if i==dic[j]:
            x[j]=i
print(x)

k={}
for i in a:
    for j in dic:
        if i==dic[j]:
            k[j]=i
print(k)             
