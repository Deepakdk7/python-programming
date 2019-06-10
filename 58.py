ax=input().split()
bx=input().split()
k=int(ax[1])
bx=list(map(int,bx))
if k in bx:
    print("yes")
else:
    print("no")
