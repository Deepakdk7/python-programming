ax=input()
ax=ax.split()
ax=list(map(int,ax))
a1=ax[0]
a2=ax[1]
for n in range(a1+1,a2):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,"",end="")
