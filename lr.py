x1,x2=map(int,input().split())
for j in range(1,10001):
  if((j%x1==0) and (j%x2==0)):
    print(j)
    break
