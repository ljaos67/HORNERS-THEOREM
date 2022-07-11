#!/usr/bin/env python
# coding: utf-8

# Math 435
# Leo Jaos
# 02/24/2022
# Assign 2.6

# 1). Determine how many flops (algebraic operations) we will need to evaluate P(x) at x0 directly.

# P(x0) = an*(X0^n) + an-1*(X0^n-1) + ... + a1*x0 + a0
# 
# piece by piece
# 
# for each x^n term -> x^n = x*x*x*...*x -> (n-1)! operations
# Each term has a multiplier: an -> n
# Add each term: -> n
# 
# total flops for a polynomial of degree n: 
# <br>(n-1)! + 2n
# 
# at x0 -> P(x) = a1x0 + a0
# 
# 2 flops
# 
# 

# 2). Determine how many flops we will need to evaluate P(x) at x0 by using Horner’s Method
# 
# Horners formular: 
# P(x) = (x - x0)Q(x) + b0
# P(x0) = (x0 - x0)*Q(x0) + b0
# 
# p(x0) = b0 (In proof)
# 
# zero flops to evaluate P(x0), we know it equals b0 through the proof.
# 

# 3). Consider the problem to find x such thatWhen the Newton’s method is being used to find an approximate zero of a polynomial, P(x)
# and P0(x) can be evaluated. Based on the before items 1. and 2. compute how many flops we
# will need to apply 10 iterations of Newton Method by evaluating P(x) and P0(x) (a) directly
# and (b) via Horner’s Method. Here you can assume that the calculation of the coefficients of
# P0 is free.
# 
# a). Let n be the degree of p(x) 
# 
# Then p(x) has (n-1)! + 2n flops
# 
# then p'(x) = n*(an)x^n + n-1*(an-1)*x^n + ... + a1
# 
# coffcients of p'(x) are fre
# 
# which would equal (n-2)! + 2(n-1) flops
# 
# plus a division and adding flop for each iteration
# for 10 iterations
# 
# 10((n-1)! + 2n + (n-2)! + 2(n-1) + 2)
# 
# = 10((n-1)! + (n-2)! + 4n) flops to evaluate the polynomial directly
# 
# at x0
# 
# xk+1 = x - (a1x0 + a0)/b2x + b1
# 
# 10 * 6 = 60 flops
# 
# b). Horner's method
# 
# xk+1 = x - (p(x0))/(p'(x0))
# 
# xk+1 = x - b0/b1x0 + b1
# 
# 10 * 4 = 40 flops
# 

# 4). Implement the Newton Method efficiently by using Horner Method to evaluate
# 
# P(x) and P0(x) creating a function in JULIA as follows:
# 
# 5). Use it to find the zeros of x5 􀀀 x4 + 2x3 􀀀 3x2 + x 􀀀 4 with a tolerance <br>10-8.
# 
# 6). Use it to find the critical points of x4 + 2x3 􀀀 3x2 + x 􀀀 4 with a <br> tolerance 10-8.

# In[15]:


print("4). Implemented Horner's and newtons in python--\n")
import math

def horner(poly, n, x):
    
    result = poly[0]
    
    for i in range(1,n):
        result = result*x + poly[i]
    return result
poly = [1, -1, 2, -3, 1, -4]
poly2 = [5,-4,6,-6,1]
n2 = len(poly2)
n = len(poly)
print("5).")
x = 0
chk = True
Tol = 10**-8
cnt = 1;
while(chk):
    x0 = x
    x = x0 - (horner(poly, n, x0))/(horner(poly2, n2, x0))
    if(abs(x - x0) <= Tol*(1 + abs(x0))):
        chk = False
    print("\tapproximation %d: %2.8f" % (cnt,x))
    cnt+=1
print("Zero for x^5 - x^4 + 2x^3 - 3x^2 + x -4: \n\t %5.9f in %d iterations\n\n" % (x,cnt) )
print("6).")
poly = [1,2,-3,1,-4]
poly2 = [4,6,-6,1]
n2 = len(poly2)
n = len(poly)

x = 0
chk = True
Tol = 10**-8
cnt = 1;
while(chk):
    x0 = x
    x = x0 - (horner(poly, n, x0))/(horner(poly2, n2, x0))
    if(abs(x - x0) <= Tol*(1 + abs(x0))):
        chk = False
    print("\tapproximation %d: %2.8f" % (cnt,x))
    cnt+=1
print("Zero for x^4 + 2x^3 -3x^2 + x - 4: \n\t %5.9f in %d iterations" % (x,cnt) )

