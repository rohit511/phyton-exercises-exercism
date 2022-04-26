def distance(strand_a, strand_b):
    #  Throw error for edge case.
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    #  Find number of differences.
    differences = 0
    for letter_idx in range(len(strand_a)):
        if strand_a[letter_idx] != strand_b[letter_idx]:
            differences += 1
    return differences