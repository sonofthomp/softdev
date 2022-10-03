import random

opened_file = open('occupations.csv', 'r')
content = opened_file.read()

lines = content.split("\n")

percentages = {}

for line in lines:
    if line == "" :
        continue
    if line[0] == "\"" :
        job_percent = line.split("\",")
    else:
        job_percent = line.split(",")

    job = job_percent[0]
    percent = job_percent[1]
    percentages[job] = percent
    
total = percentages["Total"]

percentages.pop("Job Class")
percentages.pop("Total")

r = random.random() * float(total)

sum = 0
for key in percentages:
     sum += float(percentages[key])
     if r < sum:
        if key[0] == "\"" :
            key = key[1:]
        print(key)
        break
