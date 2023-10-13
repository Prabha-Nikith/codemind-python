n=int(input())
list1=list(map(int,input().split()))
sum1=0
for i in list1:
    if(i%2!=0):
        sum1+=i
print(sum1)