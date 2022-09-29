def string_match(a, b):
  count = 0
  length = min(len(a), len(b))
  for i in range(length - 1):
    if a[i:i+2] == b[i:i+2]:
      count+=1
  return count

print(string_match('xxcaazz', 'xxbaaz') == 3)
print(string_match('abc', 'abc') == 2)
print(string_match('abc', 'axc') == 0)
print(string_match('hello', 'he') == 1)
print(string_match('he', 'hello') == 1)
print(string_match('h', 'hello') == 0)
print(string_match('', 'hello') == 0)
print(string_match('aabbccdd', 'abbbxxd') == 1)
print(string_match('aaxxaaxx', 'iaxxai') == 3)
print(string_match('iaxxai', 'aaxxaaxx') == 3)