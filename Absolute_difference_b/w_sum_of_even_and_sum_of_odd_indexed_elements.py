n=int(input())
list1=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(len(list1)):
    if(i%2==0):
        sum1+=list1[i]
    if(i%2!=0):
        sum2+=list1[i]
print(abs(sum1-sum2))