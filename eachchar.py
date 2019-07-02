inp1=input()
inp2=''
inp3='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in inp1:
    if i in inp3:
        inp4=inp3.index(i)
        inp4=inp4+3
        inp2=inp2+inp3[inp4]
print(inp2)
