def string_splosion(str):
  counter = 0
  final = ""
  while counter < len(str):
    final+=str[0:counter+1]
    counter+=1
  return final