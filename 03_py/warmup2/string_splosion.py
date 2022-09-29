def string_splosion(str):
  counter = 0
  final = ""
  while counter < len(str):
    final+=str[0:counter+1]
    counter+=1
  return final

print(string_splosion('Code') == 'CCoCodCode')
print(string_splosion('abc') == 'aababc')
print(string_splosion('ab') == 'aab')
print(string_splosion('x') == 'x')
print(string_splosion('fade') == 'ffafadfade')
print(string_splosion('There') == 'TThTheTherThere')
print(string_splosion('Kitten') == 'KKiKitKittKitteKitten')
print(string_splosion('Bye') == 'BByBye')
print(string_splosion('Good') == 'GGoGooGood')
print(string_splosion('Bad') == 'BBaBad')