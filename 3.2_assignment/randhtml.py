#Joy Elias 

import flask
import random
import os

app = flask.Flask(__name__)

@app.route("/")
def index(): 
    ran_number = random.randint(1, 100)
    return "<h3>" + str(ran_number) + "</h3>"
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)



