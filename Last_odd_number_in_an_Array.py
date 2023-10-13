def oddNum(l1,n):
    for i in  range(n-1,-1,-1):
        if l1[i]%2!=0:
            return l1[i]
    return 0
n=int(input())
l1=list(map(int,input().split()))
print(oddNum(l1,n))