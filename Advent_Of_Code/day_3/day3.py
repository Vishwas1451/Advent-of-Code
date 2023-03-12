'''
f=open('./input.txt','r')
x=f.readlines()
y=0
for i in x:
  q=int(len(i)/2)
  a=i[:q]
  b=i[q:]
  p=''
  for j in range(0,len(a)):
    if b.count(a[j])>0:
      p=a[j]
      break
  if p.isupper():
    y+=ord(p)+27-65
  else:
    y+=ord(p)-96      
f.close()
print(y)
'''

f=open('./input.txt','r')
x=f.readlines()
y=0
for i in range(0,(len(x)),3):
    a=x[i]
    b=x[i+1]
    c=x[i+2]
    p=''
    for j in range(0,len(a)):
      if b.count(a[j])>0 and c.count(a[j])>0:
         p=a[j]
         break
    if p.isupper():
       y+=ord(p)+27-65
    else:
       y+=ord(p)-96    
     
f.close()
print(y)

