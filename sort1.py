a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
c=0
while b!=[]:
    if(b[0]+a[1])in b and (b[0]+2*a[1]) in b:
        c=c+1
        b.pop(0)    
    else:
        b.pop(0)
print(c)
