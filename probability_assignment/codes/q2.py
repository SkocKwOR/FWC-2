from math import comb

dist=[]
p = 1/2
q = 1/2
n = 3
flRange = range(n+1)

for i in flRange:
    val = comb(n,i)*(p**i)*(q**(n-i))
    dist.append(round(val,n))

print(dist)
