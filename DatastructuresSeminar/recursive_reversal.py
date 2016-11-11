'''
Jan Simon Scheddler

Algorithms and Datastructures 
Homework 1
WS 20016/17
'''

def recursive_reversal(lst):
    #if it's an empty list there is nothing to reverse...
    if (len(lst) == 0):
        return []
    #reversal: take the last list element and append to it a reversed sub-list
    result = [lst[-1]]+recursive_reversal(lst[:-1])
    return result

#just testing stuff.
list1 = list(range(0,10))
backwards = list(range(9,-1,-1))
backwards2 = recursive_reversal(list1)

print("List:", list1)
print("Backwards(sample)", backwards)
print("Backwards(function)", backwards2)
