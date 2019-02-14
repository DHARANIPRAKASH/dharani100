a=int(input("enter a number"))
e=0
b=0
c=a
while(a>0):
    e =(a % 10)
    b=(e*e*e)+b
    a=a//10
if(b==c):
    print("yes")
else:
    print("no")
        
    
