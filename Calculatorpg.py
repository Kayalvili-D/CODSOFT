#Calculator Program
def calculator(a,b):
    if select=='add':
        return a+b
    elif(select=='sub'):
        return a-b
    elif(select=='mul') :
        return a*b
    elif(select=='div'):
        if (b==0):
            return 0
        return a/b
    else:
        exit()
a=int(input("enter a"))
b=int(input("enter b"))
select=input("select operation : ") 
print(calculator(a,b))   
