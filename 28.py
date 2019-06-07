ax=int(input())
bx=input()
bx=bx.split()
bx=list(map(int,bx))
for i in bx:
    print(i,bx.index(i))
