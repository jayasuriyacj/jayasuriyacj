x1=int(input())
x2=0
x3=[]
for k in range(x1):
  x3.append(input())
for k in range(x1):
  if(sorted(x3[k])==sorted('kabali')):
    x2=x2+1
print(x2)
