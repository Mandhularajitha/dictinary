dic= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
a=list(dic.keys())
b=list(dic.values())
print(a)
l=[]
for i in a:
    s=""
    for j in i:
        if j==" ":
            pass
        else:
            s+=j
    l.append(s)
d={}
for i in b:
    for j in l:
        d[j]=i
print(d)


