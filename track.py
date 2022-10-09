a=int(input())
b=[]
for i in range(1,a):
    if(a%i==0):
        b.append(i)
if(sum(b)==a):
    print("Yes")
else:
    print("No")
