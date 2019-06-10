ax=input().split()
ax=list(map(int,ax))
a=abs(ax[0]-ax[1])
if(a%2==0):
    print("even")
else:
    print("odd")
