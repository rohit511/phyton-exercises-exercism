def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')
    if sum(1 for d in digits if d < 0 or d >= input_base):
        raise ValueError('all digits must satisfy 0 <= d < input base')
    n = sum(d*input_base**(len(digits)-i-1) for i,d in enumerate(digits))
    
    output = []
    while True:
        d = n % output_base
        n = (n - d) / output_base
        output.insert(0, d)
        if n == 0:
            break
    return output