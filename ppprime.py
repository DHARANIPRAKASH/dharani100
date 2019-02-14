l = int(input("Enter lower range: "))
u = int(input("Enter upper range: "))

print("Prime numbers between",l,"and",u,"are:")

for n in range(l,u + 1):
 
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
