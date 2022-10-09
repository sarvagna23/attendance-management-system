print('☻ ☻ ♥ F L A M E ♥ ☻ ☻\n') 
a=input('Enter chekn name     :') 
b=input('Enter chekkathi name :') 
a=a.replace(' ','') 
b=b.replace(' ','')
z=0
print(a,b) 
d='.......B E   P A T I E N T   M O N U .......' 
for j in range(len(d)): 
    for i in range(4000): 
        pass 
    print(d[j],end='') 
 
    for i in range(2000): 
        pass 
print('\n\n') 
c=a+b 
i=0 
print(c) 
l=['F','L','A','M','E'] 
print('Starting with',l,'\n') 
for i in range(5,1,-1):
    d=  (len(c))%(i+z)
    z=d-1
    if d==0: 
        print(l.pop(),' is crossed out') 
    else: 
        print(l.pop(d-1),'is crossed out') 
    print('Remaining in flame--',l) 
    if i==3: 
        input('\nHAPPY or SAD ?') 
        print('Happy or Sad..... no one cares.. REMEMBER..its ur DUTY to be HAPPY') 
    if i>2: 
        input('[---press ENTER to move forward---]\n') 
if l[0]=='F': 
    print('At the end both of them will be FRIENDS') 
elif l[0]=='L': 
    print('At the end both of them will be LOVE\nHey BRO dont be that happy ....') 
elif l[0]=='A': 
    print('At the end both of them will be ANGRY') 
elif l[0]=='M': 
    print('At the end both of them will get MARRIED') 
elif l[0]=='E': 
    print('At the end both of them will be ENEMIES') 
 
 
input()
