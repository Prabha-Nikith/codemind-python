n=int(input())
l1=list(map(int,input().split()))
a=int(input())
c=0
for i in range(0,n):
    if a==l1[i]:
        c+=1
print(c)