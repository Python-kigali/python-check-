'''
    You will be given a number and you will need to return it as
    a string in Expanded Form.
'''

def expanded_form(num):
    ''' Write a number in expanded form. '''
    result = []

    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))

    return ' + '.join(result[::-1])

# Test cases
expanded_form(12)
expanded_form(42)
expanded_form(70304)
