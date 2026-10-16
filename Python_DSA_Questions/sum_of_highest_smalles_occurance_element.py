def sumOfFrequencies(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0) + 1
    counts = sorted(set(freq.values()))
    largest = counts[-1]
    smallest = counts[0]
    return largest + smallest
print(sumOfFrequencies([1, 2, 2, 3, 3, 3, 4, 4]))