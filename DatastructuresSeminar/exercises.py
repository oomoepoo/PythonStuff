import time
def find_occurence(lst,int):
    for (i in range(0, len(lst)):
        if (lst(i) == int):
            return i
    return -1

def sum_list(lst)
    result = 0
    for elem in lst:
        result = result + elem
    return result

# if you define multiplication yourself, this becomes polynomial instead of O(n)
def power_of_x(x,n):
    result=1
    for i in range(0,n):
        result = result*x
    return result

def recursive_power_of_x(x,n):
    if (n == 0):
        return 1
    return x*recursive_power_of_x(x,n-1)
    
test_lst=[0 for x in range(0,100000000)]
test_lst.append(1)

before1 = time.clock()
print find_occurence(test_lst,1)
after1 = time.clock()
print ("time for the custom function: ")
print (after1-before1)
before2 = time.clock()
print test_lst.index(1)
after2 = time.clock()
print ("time for the built-in function: ")
print (after2-before2)
#x^2 = x*x
testx = 5000
textn= 5000
before1=