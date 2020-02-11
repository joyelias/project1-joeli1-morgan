# import flask
# import os

# app = flask.Flask(__name__)

# @app.route('/')  
# def index(): 
#     return flask.render_template("index.html")

# app.run(
#     port=int(os.getenv('PORT', 8080)),
#     host=os.getenv('IP', '0.0.0.0'),
#     debug=True
# )

import flask
import os
import requests
import random
import requests_oauthlib
import json


app = flask.Flask(__name__)


@app.route('/') 
def index(): 
    #Set Up Twitter API
    twitter_url = "https://api.twitter.com/1.1/search/tweets.json?q=Beyonce"
    random_tweet = random.randint(0,14)
    oauth = requests_oauthlib.OAuth1(
        "1g57GGgJ7CBOPpGooj9MUKYFk", 
        "C9aFUfRIT1Ad0nB9DN4N0Cn0iQ114kXn2t8dM72NGk0ZH1eoiz",
        "325816963-BpjzgaU98fPHtZknAK1X9Oq3QxSmflHE44cJu6hC",
        "skAgcoC7tIh2GuLReMrCx5iO60gWz0vT4sh2fnqQs4FFr"
    )
    response = requests.get(twitter_url, auth=oauth)
    json_body = response.json()
    tweets_about_beyonce = json_body['statuses'][random_tweet]['text']
    print(response.json())
    

    #Set Up Spoontacular
    #basic information
    # spoonacular_api = "https://api.spoonacular.com/recipes/search?query=cheese&number=2"
    # my_headers = {"Authorization": "Bearer 9Z1vNErMoWax7Ly0N4_lofj35lnP2NOgDVde0C0h8M5HO0sh09sggU0rXwhDFOQU"}
        
    # response = requests.get(spoonacular_api)
    # json_body = response.json()
    # print(json_body["results"][0]["title"])


    # return flask.render_template("index.html", song = song, pic= pic, artist = artist, tweets_about_beyonce= tweets_about_beyonce)
    return flask.render_template("index.html")
    
    
app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'))