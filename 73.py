ax=int(input())
x=input().split()
x=list(map(int,x))
if(ax in range(x[0]+1,x[1])):
   print('yes')
else:
   print('no')
