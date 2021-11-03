a = {(1,2):1,(2,3):2}
print(a[1,2])

# out put 1
# ==================================================
a = {'a':1,'b':2,'c':3}
print(a["c"])

# ===================================================

fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1

addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print (len(fruit))
print(fruit)

#=======================================================================


box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print (len(crates[box]))