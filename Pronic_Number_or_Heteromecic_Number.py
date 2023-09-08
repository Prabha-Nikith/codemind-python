a=int(input())
for i in range(1,a+1):
    if(i*(i+1)==a):
        break
if(i*(i+1)==a):
    print("YES")
else:
    print("NO")