import math
import random
import sys
U = math.pow(10,10)
def ktr_nto(x):
    if x<4:
        return x>1
    else:
        dv = math.sqrt(x)
        for i in range(2,int(dv)+1):
            if x%i==0:
                return False
        return True

def find_nto(u): #thuat toan tim so nguyen to be nhat lon hon |U|
    while True:
        if ktr_nto(u):
            return u
        else:
            u=u+1

class Hash_ab:
    def __init__(self,u,n):
        self.u = u
        self.n = n
        p = find_nto(n)
        self.p = p
        self.a = random.randint(0, p)
        self.b = random.randint(0,p - 1)
    def hash(self,x):
        return ((self.a*x + self.b)%self.p)%self.n

class Hash_a:
    def __init__(self, u, b):
        self.u = int(u)
        self.b = int(b)
        self.Arr = [[0]*self.u]*self.b
        for i in range(self.b):
            for j in range(self.u):
                self.Arr[i][j] = random.randint(0,1)
    def hash(self,ss):
        if len(ss)<self.u:
            for i in range(len(s),self.u):
                ss.append(0)
        res = [0]*self.b;
        for i in range(self.b):
            for j in range(self.u):
                res[i]=(res[i]+self.Arr[i][j]*ss[i])%2
        return res

has = Hash_ab(int(U),100)
a = [0 for i in range(has.n)]
b = [0]*has.n
for i in range(2000):
    x = random.randint(0, U)
    x = has.hash(x)
    a[x] = a[x] + 1


dem = 0
for i in range(100):
    print '\n%d: ' %(i+1)
    for j in range(a[i]):
        sys.stdout.write('|')
        dem=dem+1
print dem
has2 = Hash_a(100,10)
for i in range(1000):
    ss = [random.randint(0,1) for i in range(100)]
    print has2.hash(ss)