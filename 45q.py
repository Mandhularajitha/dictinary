l=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

s='#FF0000'
list=[]
for i in l:
    if s in i.values():
        pass
    else:
        list.append(i)
print(list)

