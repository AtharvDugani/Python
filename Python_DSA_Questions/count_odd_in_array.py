def count_odd_in_array(arr):
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count
print(count_odd_in_array([1, 2, 3, 4, 5]))
