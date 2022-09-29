def front_back(str):
  if (len(str) <= 1):
    return str
  return str[-1] + str[1:-1] + str[0]

print(front_back('code') == 'eodc')
print(front_back('a') == 'a')
print(front_back('ab') == 'ba')
print(front_back('abc') == 'cba')
print(front_back('') == '')
print(front_back('Chocolate') == 'ehocolatC')
print(front_back('aavJ') == 'Java')
print(front_back('hello') == 'oellh')