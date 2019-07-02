inp1=str(input())
inp3=0
a=['a','e','i','o','u']
for i in a:
  if(i in a):
    inp1=inp1.replace(i,'')
print(inp1[::-1])
