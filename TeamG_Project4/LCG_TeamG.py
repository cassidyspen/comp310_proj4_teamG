"""
LCG_TeamG.py
Team G's implementation of Linear Congruential Generator (LCG)
Names:Ajay Samra, Claire Ingrey, Cassidy Spencer, Kevin Nhu, and Katrina Baha
Date: 5/2/22
"""
import datetime

today = datetime.datetime.now()
now = today.second

#formula: x(i+1) = (a * x(i) + c) mod m
#xi = seed number (now is xi)
#a = multiplier
#c = increment
#m = modulus

#source: https://dl.acm.org/doi/pdf/10.5555/2955239.2955463 on 5/2/22
m = 22873
a = 6943
c = 5593

def LCG_TeamG(seed):
    random_num = (a * seed + c)%m
    return random_num 
