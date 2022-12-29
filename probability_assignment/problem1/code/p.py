import numpy as np
#rng = np.random.default_rng(12345)
s = 10000
ps = 10/10000
qs = 1-ps
n= int(input())
count = 0
for i in range(s):
    trail = np.random.choice([0,1],n,p=[qs,ps])
    if(np.count_nonzero(trail)>0):
        count +=1
prob = count/s
print(1-prob)
