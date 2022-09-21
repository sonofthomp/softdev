def sum2(nums):
  if len(nums) == 0:
    return 0
  count = 0
  length = min(len(nums), 2)
  for i in range(length):
    count += nums[i]
  return count