#part1
f=open('./input.txt','r')
x=f.readlines()
index=0
for i in range(0,len(x[0])-3):
    if ((x[0][i])==(x[0][i+1])) or ((x[0][i])==(x[0][i+2])) or ((x[0][i])==(x[0][i+3])) or ((x[0][i+1])==(x[0][i+2])) or ((x[0][i+1])==(x[0][i+3])) or ((x[0][i+2])==(x[0][i+3])) :
        continue
    else:
        index=i+4
        break

print(index)   
f.close()
#part2
f=open('./input.txt','r')
x=f.readlines()
index=0
for i in range(0,len(x[0])-3):
    l=x[0][i:i+14]
    l1=[]
    for j in range(14):
        l1.append(l[j])
    s=set(l1)
    if len(s)==len(l1):
        index=i+14
        break
print(index)
f.close()
