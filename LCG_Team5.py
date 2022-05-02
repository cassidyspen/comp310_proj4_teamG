"""
LCG_Team5.py
Team 5's implementation of Linear Congruential Generator (LCG)
Names:Ajay Samra, Claire Ingrey, Cassidy Spencer, Kevin Nhu, and Katrina Baha
Date: 5/2/22
"""
import time

now = round(time.time())

#x(i+1) = (a * x(i) + c) mod m
#xi = seed number (maybe w/ clock)
#a = multiplier
#c = increment
#m = modulus

#source: ZX81
x_initial = now
m = (2**31) - 1
a = 16807
c = 0

def LCG_Team5():
    random_num = (a * x_initial + c)%m
    return random_num 

if __name__ == "__main__":
    rm = LCG_Team5()
    print (rm)