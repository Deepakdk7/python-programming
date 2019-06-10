ax=input()
ax=ax[::-1]
ax=int(ax)
while ax!=0:
    r=ax%10
    print(r,"",end="")
    ax=ax//10
