ax=int(input())
if ax%2==0:
    print(ax)
else:
    while ax!=0:
        ax=ax-1
        if ax%2==0:
            print(ax)
            break
