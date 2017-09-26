def equals(a,b):
    if a==b:
        return True
    else:
        return False

def majority_element(list):
    n = len(list)
    mid = (n-1)/2
    if n<=1:
        return list[0]
    m1 = majority_element(list[0:mid+1])
    m2 = majority_element(list[mid+1:n])
    count = 0
    for a in list:
        if equals(m1,a):
            count+=1
    if count > n/2+1:
        return m1
    else:
        return m2
list = [2,2,2,2,2,5,0,1,2,3,4,5]

result = majority_element(list)

print result