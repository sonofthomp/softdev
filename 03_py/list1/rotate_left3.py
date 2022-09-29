def rotate_left3(nums):
  arr = []
  
  for i in range(len(nums)):
    if i != len(nums)-1:
      arr.append(nums[i+1])

  arr.append(nums[0])
  return arr

print(rotate_left3([1, 2, 3]) == [2, 3, 1])
print(rotate_left3([5, 11, 9]) == [11, 9, 5])
print(rotate_left3([7, 0, 0]) == [0, 0, 7])
print(rotate_left3([1, 2, 1]) == [2, 1, 1])
print(rotate_left3([0, 0, 1]) == [0, 1, 0])