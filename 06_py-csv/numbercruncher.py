import random

content = open('occupations.csv', 'r').readlines()
content = content[1:]

occupations = {}

for line in content:
	end_comma_index = line[::-1].index(',')
	comma_index = len(line) - end_comma_index
	occupation = line[:comma_index - 1]
	percent = float(line[comma_index:])

	occupations[occupation] = percent

print(occupations)
