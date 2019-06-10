ax=input().split()
bx=input().split()
k=int(ax[1])
c=0
bx=list(map(int,bx))
for i in bx:
    if k==i:
        c=c+1
print(c)
