f=open('./input.txt','r')
x=f.readlines()
y=[]
print(x[0])
sum=0
for i in x:
 if i.strip()=='':  
   y.append(sum)
   sum=0  
 else:  
   sum +=int(i[:len(i)-1])
f.close()
y.sort()
print(y[-1]+y[-1]+y[-3])