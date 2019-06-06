ax=input()
ax=ax.split()
ax=list(map(int,ax))
bx=ax[0]
cx=ax[1]
for i in range(bx+1,cx+1):
    if i%2!=0:
        print(i,"",end="")
