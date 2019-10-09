def max_sequence(seq):
    max = sum(seq[0:5])
    sequence = seq[0:5]
    for i in range(len(seq) - 5):
        if max < sum(seq[i:i + 5]):
            max = sum(seq[i:i + 5])
            sequence = seq[i:i + 5]

    print(sequence)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
