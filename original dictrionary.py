
a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
s=[]
d={}
for i,j in a.items():
    for k in j: 
        d[i]=k
s.append(d)
print(s)



l=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
dict={}
for i in l:
    dict[i[0]]=i[1:]
    dict.update(dict)
print(dict)