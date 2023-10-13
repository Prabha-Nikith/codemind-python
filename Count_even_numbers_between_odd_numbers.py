n=int(input())
l1=list(map(int,input().split()))
c=0
for i in range(n-2):
    if l1[i]%2!=0 and l1[i+2]%2!=0 and l1[i+1]%2==0:
        c+=1
    else:
        i+=1
print(c)