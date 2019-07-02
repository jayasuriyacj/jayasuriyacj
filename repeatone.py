x1=int(input())
x2=list(map(int,input().split()))
count=0
for j in range(0,x1+1):
  if(x2.count(j)==1):
   print(j)
   break
