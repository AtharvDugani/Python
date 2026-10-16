def highestOccurringElement(nums):
    # Write your code here
    largest = 0
    element = nums[0]
    for i in nums:
        count = nums.count(i)
        if count > largest or (count == largest and i < element):
            largest = count
            element = i
    return element

print(highestOccurringElement([1, 2, 2, 3, 3, 3, 4, 4]))