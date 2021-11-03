d= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

s=[]
a,b=d.values()

for i in range(len(a)):
    for j,k in d.items():
        b=({j:k[i]})
        s.append(b)
print(s)