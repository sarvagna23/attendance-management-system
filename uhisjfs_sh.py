import array

a=int(input())
while(a):
    a-=1
    num,sum=map(int,input().split())
    arr=list(map(int,input().split()))
    print(arr)
    win_sum,win_start=0

    for i in range(arr.size()):
        win_end+=1
