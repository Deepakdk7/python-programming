ax=input().split()
bx=input().split()
ax=list(map(int,ax))
bx=list(map(int,bx))
m1=ax[0]*60+ax[1]
m2=bx[0]*60+bx[1]
m=abs(m1-m2)
h=m//60
m=m-(h*60)
print(h,m)
