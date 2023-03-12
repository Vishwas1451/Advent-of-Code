'''
f=open('./input.txt','r')
x=f.readlines()
y=0
for i in x:
   if i[0]=='A' and i[2]=='X':
     a=1+3
     y+=a
   elif i[0]=='A' and i[2]=='Y':
     a=2+6
     y+=a 
   elif i[0]=='A' and i[2]=='Z':
     a=3+0
     y+=a 
   elif i[0]=='B' and i[2]=='X':
     a=1+0
     y+=a 
   elif i[0]=='B' and i[2]=='Y':
     a=2+3
     y+=a  
   elif i[0]=='B' and i[2]=='Z':
     a=3+6
     y+=a 
   elif i[0]=='C' and i[2]=='X':
     a=1+6
     y+=a
   elif i[0]=='C' and i[2]=='Y':
     a=2+0
     y+=a 
   elif i[0]=='C' and i[2]=='Z':
     a=3+3
     y+=a               

f.close()
print(y)
'''
f=open('./input.txt','r')
x=f.readlines()
y=0
for i in x:
   if i[0]=='A' and i[2]=='X':
     a=3+0
     y+=a
   elif i[0]=='A' and i[2]=='Y':
     a=1+3
     y+=a 
   elif i[0]=='A' and i[2]=='Z':
     a=2+6
     y+=a 
   elif i[0]=='B' and i[2]=='X':
     a=1+0
     y+=a 
   elif i[0]=='B' and i[2]=='Y':
     a=2+3
     y+=a  
   elif i[0]=='B' and i[2]=='Z':
     a=3+6
     y+=a 
   elif i[0]=='C' and i[2]=='X':
     a=2+0
     y+=a
   elif i[0]=='C' and i[2]=='Y':
     a=3+3
     y+=a 
   elif i[0]=='C' and i[2]=='Z':
     a=1+6
     y+=a               

f.close()
print(y)

