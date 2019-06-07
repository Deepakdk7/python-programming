dx=int(input())
cx=input()
cx=cx.split()
cx=list(map(int,cx))
cx.sort()
for i in cx:
    print(i,"",end="")
