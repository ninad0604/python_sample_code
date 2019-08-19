"""
"""


# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):

    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                result.append(array[i])
                result.append(array[j])
                break

    return sorted(result)

# O(n) time | O(n) space
def twoNumberSum1(array, targetSum):
    numbers = {}

    for n in array:
        if targetSum - n in numbers:
            return sorted([n, targetSum-n])
        else:
            numbers[n] = True
    return []

# O(nlogn) time | O(1) space
def twoNumberSum2(array, targetSum):
    array = sorted(array)
    left = 0
    right = len(array)-1
    while left< right:
        curr_sum = array[left] + array[right]
        if curr_sum == targetSum:
            return [array[left],array[right]]
        elif curr_sum < targetSum:
            left += 1
        elif curr_sum > targetSum:
            right -= 1


    return []
