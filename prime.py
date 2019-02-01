a=int(input("enter number"))
b=0
for i in range(1,a+1,1):
    if((a%i)==0):
            b=b+1
if(b==2):
      print("yes")
else:
      print("no")
      
