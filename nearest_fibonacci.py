a=int(input())
b=0
c=1
d=0
while(a>c):
    d=b+c
    b,c=c,d
if(c==d):
    c=b
k=a-c
l=d-a
if k>l:
    print(d)
elif l>k:
    print(c)
else:
    print(c,d)