    
ax=input().split()
ax=list(map(int,ax))
ax[0]=ax[0]+ax[1]
ax[1]=ax[0]-ax[1]
ax[0]=ax[0]-ax[1]
for i in ax:
    print(i,"",end="")
