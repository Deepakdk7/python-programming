ax=input()
ax=ax.split()
ax=list(map(int,ax))
n=ax[0]
a=ax[1]
d=ax[2]
s = (n * (2 * a + (n - 1) * d)) // 2
print(s)
