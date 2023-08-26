a=int(input())
b=int(input())
s=0
t=0
for i in range (1,a):
    if(a%i==0):
        s=s+i
for f in range (1,b):
    if(b%f==0):
        t=t+f
if(a==t and b==s):
    print("Amicable")
else:
    print("Not Amicable")