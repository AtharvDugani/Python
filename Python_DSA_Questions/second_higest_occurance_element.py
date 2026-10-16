def secondHighestOccurringElement(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0)+1
    counts = sorted(set(freq.values()), reverse = True)
    second_largest = counts[1]
    matching_element = []
    for i in freq:
        if freq[i] == second_largest:
            matching_element.append(i)
    return min(matching_element)

print(secondHighestOccurringElement([1, 2, 2, 3, 3, 3, 4, 4]))