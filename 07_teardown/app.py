"""
Chicken Fries (Mahir Riki, Vivian Teo, Gabriel Thompson)
SoftDev
K07 -- Teardown
2022-10-03 => 2022-10-0X
time spent: X.X hours
"""

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. 
1. '/' : seen it when accessing directories, it's like a pathway for where you want to go
2. It'll print to the title of the webpage
3. 127.0.0.1:5000/
4. This'll appear on the webpage. I know because I tested this and saw for myself
5. 
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 - app = Flask(__name__) : creates the app kind of, like an initiation thing
 - @app.route("/") : the route of the webpage so like "/about" would take you to the ab page
 - the function directly below the route returns what gets printed on the page
 - you can use the functions because you can pass in parameters and make site more interactive
 
'''

