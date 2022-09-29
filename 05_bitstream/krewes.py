""" 
Gitae Park, Gabriel Thompson
SoftDev
05_bitstream
2022-09-28
time spent: 0.1 hours

DISCO: 
 - 

QCC:
 - 

OPS SUMMARY:
 1. 
"""

f = open('krewes.txt')
content = f.read()[:-1]
periods = {}

for devo in content.split('@@@'):
	details = devo.split('$$$')
	period = int(details[0])
	name = details[1]
	ducky = details[2]

	if not periods.get(period):
		periods[period] = {}

	periods[period][name] = ducky

print(periods)
