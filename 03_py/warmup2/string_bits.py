def string_bits(str):
  return str[::2]

print(string_bits('Hello') == 'Hlo')
print(string_bits('Hi') == 'H')
print(string_bits('Heeololeo') == 'Hello')
print(string_bits('HiHiHi') == 'HHH')
print(string_bits('') == '')
print(string_bits('Greetings') == 'Getns')
print(string_bits('Chocoate') == 'Coot')
print(string_bits('pi') == 'p')
print(string_bits('Hello Kitten') == 'HloKte')
print(string_bits('hxaxpxpxy') == 'happy')