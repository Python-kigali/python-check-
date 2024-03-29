'''
	- Given an array of integers, find the one that
    appears an odd number of times.

	- There will always be only one integer that appears
    an odd number of times.

    Examples
      - [7] should return 7, because it occurs 1 time (which is odd).

      - [0] should return 0, because it occurs 1 time (which is odd).

      - [1,1,2] should return 2, because it occurs 1 time (which is odd).

      - [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).

      [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1
      time (which is odd).
'''
def find_it(seq):
    '''Find the integer that appears an odd number of times in the sequence.'''
    for i, num in enumerate(seq):
        if seq.count(num) % 2 != 0:
            return num

    # single liner to find the integer that appears an odd number of times
    # return [x for x in seq if seq.count(x) % 2][0]


# def find_it(seq):
#     return [x for x in seq if seq.count(x) % 2][0]

# Test cases
print(find_it([7])) # 7
print(find_it([0])) # 0
print(find_it([1,1,2])) # 2
print(find_it([0,1,0,1,0])) # 0
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])) # 4
