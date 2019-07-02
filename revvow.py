inp1=int(input())
inp2=input()
inp3=0
a=['a','e','i','o','u']
for i in a:
  if(i in a):
    inp2=inp2.replace(i,'')
print(inp2[::-1])
