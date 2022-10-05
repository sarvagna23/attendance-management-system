T = int(input())
for i in range(T):
    A = input().split()
    N = int(A[0])
    K = int(A[1])
    X = int(A[2])
    Y = int(A[3])
    Q = ((N-K)*Y)
    W = (K*X)
    if X<Y:
        print(X*N)
    else:
        print(Q + W)
