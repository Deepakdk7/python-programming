ax=int(input())
if(ax==1 and ax==0):
    print("1")
else:
    s=1
    while ax>1:
        s=s*ax
        ax=ax-1

print(s)
