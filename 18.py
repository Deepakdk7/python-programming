ax=input()
ax=ax.split()
ax=list(map(int,ax))
a1=ax[0]
a2=ax[1]
for n in range(a1+1,a2):
    s=0
    t=n
    while n!=0:
        r=n%10
        s=s+(r*r*r)
        n=n//10
    if(t==s):
        print(s)
