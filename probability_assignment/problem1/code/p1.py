from math import comb
s = 10000
x = 9990
n = int(input())
if(n==0):
    prob = 0
if(n < x):
    prob = comb(x,n)/s
if((n>x) and (n<s)):
    prob = 1
print(prob)
