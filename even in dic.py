dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
a={}
for k,j in dic.items():
    for i in j:
        if i%2==0:
            a[k]=i
        print(a)
# not corrot a nnswer is this



