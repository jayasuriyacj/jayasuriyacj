inp1=list(map(int,input().split()))
inp2=list(map(int,input().split()))
for i in range(0,inp1[1]):
  inp2=[inp2[-1]] + inp2[:-1]
print(*inp2,end=' ')
