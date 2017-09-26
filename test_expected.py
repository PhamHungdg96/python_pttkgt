import math
import sys
import random

n = 100
number_test = 10000

def test_expected_a():
    ens = [0]*(n+1)
    expected = 0
    for i in range(number_test):
        dem = 0
        for j in range(n):
            x = random.randint(0,n-1)
            if x == j:
                dem += 1
        ens[dem] += 1
    for i in range(n+1):
        expected += i*ens[i]
    expected = float(expected)/number_test
    print "Expected homework 1a is %f and %f" %(1,expected)
def test_expected_b():
    expected = 0
    ens = [0]*(n+1)
    for i in range(number_test):
        dem = 0
        guests = [0]*n
        for j in range(n):
            x = random.randint(0,n-1)
            guests[x] +=1
        for j in range(n):
            if guests[j]==2:
                dem += 1
        ens[dem] += 1
    for i in range(n+1):
        expected += i*2*ens[i]
    expected = float(expected)/number_test
    expected_lithuyet=float(n-1)*math.pow(float(n-1)/n,n-2)
    print "Expected homework 1b is %f and %f" %(expeccted_lithuyet,expected)
    


test_expected_a()
test_expected_b()

