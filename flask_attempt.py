import flask
import os
app = flask.Flask(__name__)
@app.route('/')  
def index():
    return "Hello, Joy!"
print("I'm debugging!")
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

