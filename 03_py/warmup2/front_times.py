def front_times(str, n):
  length = min(3, len(str))
  return n*str[0:length]

print(front_times('Chocolate', 2) == 'ChoCho')
print(front_times('Chocolate', 3) == 'ChoChoCho')
print(front_times('Abc', 3) == 'AbcAbcAbc')
print(front_times('Ab', 4) == 'AbAbAbAb')
print(front_times('A', 4) == 'AAAA')
print(front_times('', 4) == '')
print(front_times('Abc', 0) == '')