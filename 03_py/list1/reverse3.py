def reverse3(nums):
  arr = []
  for num in nums:
    arr.insert(0,num)
  return arr
# return arr[::-1] is a soln too

print(reverse3([1, 2, 3]) == [3, 2, 1])
print(reverse3([5, 11, 9]) == [9, 11, 5])
print(reverse3([7, 0, 0]) == [0, 0, 7])
print(reverse3([2, 1, 2]) == [2, 1, 2])
print(reverse3([1, 2, 1]) == [1, 2, 1])
print(reverse3([2, 11, 3]) == [3, 11, 2])
print(reverse3([0, 6, 5]) == [5, 6, 0])
print(reverse3([7, 2, 3]) == [3, 2, 7])