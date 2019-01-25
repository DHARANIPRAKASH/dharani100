num=int(input("enter num"))
a=num
re=0
while(num>0):
    re =(re*10)+(num % 10)
    num = num//10
if(a==re):
    print("yes")
else:
    print("no")
 
