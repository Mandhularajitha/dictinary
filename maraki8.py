# {
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56,
# }
n=int(input("enter num"))
i=0
x={}
while i<n:
    n1=input("enterkey:")
    n2=int(input("enter value:"))
    x[n1]=n2
    i+=1
print(x)
