n=int(input())
list1=list(map(int,input().split()))
sum1=0
for i in list1:
    sum1+=i
a=sum1/n
print(f"{a:.2f}")