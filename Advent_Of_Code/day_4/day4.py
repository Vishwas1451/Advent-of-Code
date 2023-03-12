'''
f=open('./input.txt','r')
x=f.readlines()
y=0
for i in x:
 q=i.split(',')
 a=q[0].split('-')
 b=q[1].split('-') 
 p=0;u=0
 for j in range(int(b[0]),int(b[1])+1):
     if j>=int(a[0]) and j<=int(a[1]):
        p+=1
 for j in range(int(a[0]),int(a[1])+1):
     if j>=int(b[0]) and j<=int(b[1]):
        u+=1       
 if p==(int(b[1])-int(b[0])+1) or u==(int(a[1])-int(a[0])+1) :
    y+=1      

f.close()
print(y)
'''
f=open('./input.txt','r')
x=f.readlines()
y=0
for i in x:
 q=i.split(',')
 a=q[0].split('-')
 b=q[1].split('-') 
 p=0;u=0
 for j in range(int(b[0]),int(b[1])+1):
     if j>=int(a[0]) and j<=int(a[1]):
        p+=1
 for j in range(int(a[0]),int(a[1])+1):
     if j>=int(b[0]) and j<=int(b[1]):
        u+=1       
 if p>0 or u>0 :
    y+=1      

f.close()
print(y)