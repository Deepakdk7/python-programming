ax=int(input())
bx=input()
bx=bx.split()
bx=list(map(int,bx))
bx.sort()
for i in bx:
    print(i,"",end="")
