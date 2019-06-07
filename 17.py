ax=int(input())
t=ax
s=0
while ax!=0:
    r=ax%10
    s=s+(r*r*r)
    ax=ax//10
if(s==t):
    print("yes")
else:
    print("no")
