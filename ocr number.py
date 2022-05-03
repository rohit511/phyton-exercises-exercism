NUMS = [
' _     _  _     _  _  _  _  _ ',
'| |  | _| _||_||_ |_   ||_||_|',
'|_|  ||_  _|  | _||_|  ||_| _|',
'                              ']
def split_lines(nums):
    out = []
    for i in range(0, len(nums), 4):
        out.append(nums[i:i+4])
    return out
    
def split_digits(nums):
    digits = []
    digit = [[] for _ in range(4)]
    for i, z in enumerate(zip(*nums)):
        for j, zz in enumerate(z):
            digit[j].append(zz)
        if i % 3 == 2:
            digits.append([''.join(line) for line in digit])
            digit = [[] for _ in range(4)]
    return digits
def recognize_digit(digit):
    digits = split_digits(NUMS)
    if digit in digits:
        return str(digits.index(digit))
    return '?'
def convert(input_grid):
    errors = [
        'Number of input lines is not a multiple of four',
        'Number of input columns is not a multiple of three'
    ]
    if len(input_grid) % 4:
        raise ValueError(errors[0])
    if len(input_grid[0]) % 3:
        raise ValueError(errors[1])
        
    out = []
    lines = split_lines(input_grid)
    for l in lines:
        n = ''
        for d in split_digits(l):
            n += recognize_digit(d)
        out.append(n)
    return ','.join(out)
