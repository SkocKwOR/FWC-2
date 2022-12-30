import numpy as np
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
