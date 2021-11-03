dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
k=[]
for i in dic:
     for j in i.values():
          if j not in k:
               k.append(j)
               
print(k) 