# DogDino: Anjini, Gabriel, Vivian
# SoftDev
# K08 - Create a webpage with random occupation 
# 2022-10-07
# time spent: 2 hours

"""
DISCO:
 * Learned how to create a webpage from python
 * Learned how to print things to the webpage
 * Learned about modules and the importance of them
 * Learned how to html in python
 
QCC:
 * How do you make the text fancy? It looks ugly right now
 * Python = back-end, Markup language = front-end
"""
import random

from flask import Flask
app = Flask(__name__) #create instance of class Flask

def create_dict(filename):
    file = open(filename, 'r')
    content = file.read()
    #splitting the file's info by line and making it a list
    total_list = content.split('\n')
    # getting rid of first and last line
    total_list = total_list[1:-2]
    job_dict = {}

    for job in total_list:
        # for each job in the list, split it by the last comma once
        job_list = job.rsplit(',',1)
        # read the occupation title into dict as key, read the percentage into dict as value
        job_dict[job_list[0]] = float(job_list[1]) # typecast percentage from string to float
    return job_dict

def weighted_random(job_dict):
    #use python's built-in weighted random choice function to get a job title
    random_job = random.choices(list(dict.keys(job_dict)), weights=list(dict.values(job_dict)))
    # since random_job is a list consisting of one element, we can print the first element
    return random_job[0]

@app.route("/")       #assign fxn to route
def rando_job():
    # create dict of jobs
    job_dict = create_dict("occupations.csv")

    # picking rando job
    final_job = weighted_random(job_dict)

    # put list of jobs in a string so better formatting on webpage
    lizst = "<ul>"
    for job in job_dict.keys():
        if job == final_job:
            lizst += "<li><i>"+job+"</i></li>"
        else:
            lizst += "<li>"+job+"</li>"
    lizst += "</ul>"
    return "<h2>DogDino: Anjini, Gabriel, Vivian</h2>" \
           +"<br><b>Random Job: </b>"+final_job \
           +"<br><br>"+"<b>List of Jobs:</b>"+lizst
app.debug = True
app.run()

# if __name__ == "__main__":  # true if this file NOT imported
#     app.debug = True        # enable auto-reload upon code change
#     app.run()
