m=int(input())
n=list(map(int,input().split()))
o=[]
for x in range(m):
    for i in range(x+1,len(n)):
        if(n[i]==n[x]):
          o.append(n[x])
if (len(o)==0):
    print("unique")
else:
    o.sort()
    l=set(o)
    for x in l:
        print(x,end=" ")
