n=int(input())
list1=list(map(int,input().split()))
s=0
for i in list1:
   s+=i
a=s//n
if a in list1:
    print(True)
else:
    print(False)