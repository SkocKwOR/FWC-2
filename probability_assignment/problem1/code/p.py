import numpy as np
from math import comb
#simulation length
s = 10000
ps = 10/10000 #probability of wining with one ticket
qs = 1-ps     #probability of losing with one ticket
n= int(input()) #number of tickets
count = 0
for i in range(s):
    trail = np.random.choice([0,1],n,p=[qs,ps])
    if(np.count_nonzero(trail)>0):
        count +=1
prob = count/s
print(1-prob) #total probability of losing the lottery
#theoretical calculation
x = s-10
if(n==0):
    prob = 0
if(n<=x):
    prob = comb(x,n)/comb(s,n)
if((n>x) and (n<=s)):
    prob = 1
print(prob)
