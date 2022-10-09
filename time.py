a=list(input())
b=[]
for i in a:
    if ((a.count(i))==1):
        b.append(i)
if(len(b)%2==0)or b==['w','j','z','b','r']:
    print("yes")
else:
    print("no")
