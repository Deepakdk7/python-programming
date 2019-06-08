ax= int(input())
i=1
f=0
s=1
while(i < ax+1):
           if(i<=1):
                      n = i
           else:
                      n= f+ s
                      f = s
                      s = n
           print(n,"",end="")
           i = i + 1
