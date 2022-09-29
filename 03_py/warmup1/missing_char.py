def missing_char(str, n):
  if n<len(str)-1:
    return str[0:n]+str[n+1:]
  return str[0:n]

print(missing_char('kitten', 1) == 'ktten')
print(missing_char('kitten', 0) == 'itten')
print(missing_char('kitten', 4) == 'kittn')
print(missing_char('Hi', 0) == 'i')
print(missing_char('Hi', 1) == 'H')
print(missing_char('code', 0) == 'ode')
print(missing_char('code', 1) == 'cde')
print(missing_char('code', 2) == 'coe')
print(missing_char('code', 3) == 'cod')
print(missing_char('chocolate', 8) == 'chocolat')