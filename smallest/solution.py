def smallest(arr):
    '''Returns the smallest integer in a given array.'''
    return min(arr)

# Test cases
print(smallest([7])) # 7
print(smallest([0])) # 0
print(smallest([1,1,2])) # 1
print(smallest([0,1,0,1,0])) # 0
print(smallest([1,2,2,3,3,3,4,3,3,3,2,2,1])) # 1
