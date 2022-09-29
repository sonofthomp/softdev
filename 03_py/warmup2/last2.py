def last2(str):
  last = str[-2:]
  count = 0
  for i in range (len(str)-2):
    if str[i:i+2] == last:
      count+=1
  return count

print(last2('hixxhi') == 1)
print(last2('xaxxaxaxx') == 1)
print(last2('axxxaaxx') == 2)
print(last2('xxaxxaxxaxx') == 3)
print(last2('xaxaxaxx') == 0)
print(last2('xxxx') == 2)
print(last2('13121312') == 1)
print(last2('11212') == 1)
print(last2('13121311') == 0)
print(last2('1717171') == 2)
print(last2('hi') == 0)
print(last2('h') == 0)
print(last2('') == 0)