dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }

x={}    
for key,values in dic.items():
    if key not in x.keys():
        x[key]=values
print(x)