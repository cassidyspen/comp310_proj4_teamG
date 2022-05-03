"""
LCG_TeamG.py
Team G's implementation of Linear Congruential Generator (LCG)
Names:Ajay Samra, Claire Ingrey, Cassidy Spencer, Kevin Nhu, and Katrina Baha
Date: 5/2/22
"""
import datetime

today = datetime.datetime.now()
now = today.second

#x(i+1) = (a * x(i) + c) mod m
#xi = seed number (maybe w/ clock)
#a = multiplier
#c = increment
#m = modulus

#source: ZX81
#2nd source: https://dl.acm.org/doi/pdf/10.5555/2955239.2955463 on 5/2/22
#x_initial = now
m = 15
a = 106
c = 1283

def LCG_TeamG(seed):
    random_num = (a * seed + c)%m
    return random_num 

if __name__ == "__main__":
    for i in range (50):
        now = LCG_Team5(now)
        print (now)
