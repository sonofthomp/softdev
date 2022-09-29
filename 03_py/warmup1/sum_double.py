def sum_double(a, b):
  if (a == b):
    return 2*(a+b)
  else:
    return a+b

print(sum_double(1, 2) == 3)
print(sum_double(3, 2) == 5)
print(sum_double(2, 2) == 8)
print(sum_double(-1, 0) == -1)
print(sum_double(3, 3) == 12)
print(sum_double(0, 0) == 0)
print(sum_double(0, 1) == 1)
print(sum_double(3, 4) == 7)