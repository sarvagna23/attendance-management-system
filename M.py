T = int(input())
for i in range(T):
    A = input().split()
    N = int(A[0])
    K = int(A[1])
    X = int(A[2])
    Y = int(A[3])
    if X<Y:
        print(N*X)
    else:
        print((K*X)+((N-K)*Y))
