#part1
f=open('./input.txt','r')
x=f.readlines()
y=0;index=0
for i in range(0,len(x)):
  if x[i][1]=='1'  :
    y=int(x[i][-3])
    index=i
    break
d={}
for i in range(1,y+1):
   d[i]=[]
for i in range(0,index):
  for j in range(1,len(x[index]),4):
    if x[i][j]!=' ':
        d[int(j/4)+1].append(x[i][j])
for i in range(index+2,len(x)): 
    s=x[i].split(' ')
    for j in range(int(s[1])):
        a=d[int(s[3])].pop(0)
        d[int(s[5])].insert(0,a)
final=''
for i in range(1,len(d)+1):
   final +=d[i][0]
print(final)
f.close()

#part2
f=open('./input.txt','r')
x=f.readlines()
y=0;index=0
for i in range(0,len(x)):
  if x[i][1]=='1'  :
    y=int(x[i][-3])
    index=i
    break
d={}
for i in range(1,y+1):
   d[i]=[]
for i in range(0,index):
  for j in range(1,len(x[index]),4):
    if x[i][j]!=' ':
        d[int(j/4)+1].append(x[i][j])
for i in range(index+2,len(x)): 
    s=x[i].split(' ')
    for j in range(int(s[1])-1,-1,-1):
        a=d[int(s[3])].pop(j)
        d[int(s[5])].insert(0,a)
final=''
for i in range(1,len(d)+1):
   final +=d[i][0]
print(final)
f.close()