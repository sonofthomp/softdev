def parrot_trouble(talking, hour):
  if not (7<=hour<=20):
    return talking
  return False

print(parrot_trouble(True, 6) == True)
print(parrot_trouble(True, 7) == False)
print(parrot_trouble(False, 6) == False)
print(parrot_trouble(True, 21) == True)
print(parrot_trouble(False, 21) == False)
print(parrot_trouble(False, 20) == False)
print(parrot_trouble(True, 23) == True)
print(parrot_trouble(False, 23) == False)
print(parrot_trouble(True, 20) == False)
print(parrot_trouble(False, 12) == False)