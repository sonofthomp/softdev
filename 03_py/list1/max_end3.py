def max_end3(nums):
  m = max(nums[0], nums[-1])
  for i in range(len(nums)):
    nums[i] = m
  return nums

print(max_end3([1, 2, 3]) == [3, 3, 3])
print(max_end3([11, 5, 9]) == [11, 11, 11])
print(max_end3([2, 11, 3]) == [3, 3, 3])
print(max_end3([11, 3, 3]) == [11, 11, 11])
print(max_end3([3, 11, 11]) == [11, 11, 11])
print(max_end3([2, 2, 2]) == [2, 2, 2])
print(max_end3([2, 11, 2]) == [2, 2, 2])
print(max_end3([0, 0, 1]) == [1, 1, 1])