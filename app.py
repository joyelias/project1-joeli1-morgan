import flask
import os
import requests
import random
import requests_oauthlib
import json


app = flask.Flask(__name__)


@app.route('/') 
#TWITTER API SET UP
def index(): 
    twitter_url = "https://api.twitter.com/1.1/search/tweets.json?q=burger"
    random_tweet = random.randint(0,8)
    oauth = requests_oauthlib.OAuth1(
        "1g57GGgJ7CBOPpGooj9MUKYFk", 
        "C9aFUfRIT1Ad0nB9DN4N0Cn0iQ114kXn2t8dM72NGk0ZH1eoiz",
        "325816963-BpjzgaU98fPHtZknAK1X9Oq3QxSmflHE44cJu6hC",
        "skAgcoC7tIh2GuLReMrCx5iO60gWz0vT4sh2fnqQs4FFr"
    )
    response = requests.get(twitter_url, auth=oauth)
    json_body = response.json()
    tweets_about_burgers = json_body['statuses'][random_tweet]['text']
    print(response.json())
    

    #Set Up Spoontacular
    #basic information
    
    # my_headers = {"Authorization": "Bearer 9Z1vNErMoWax7Ly0N4_lofj35lnP2NOgDVde0C0h8M5HO0sh09sggU0rXwhDFOQU"}
        
    # response = requests.get(spoonacular_api)
    # json_body = response.json()
    # print(json_body["results"][0]["title"])
    
    #SPOONTACULAR API SET UP
    # playlist = random.randint(0,8)
    spoonacular_url = "https://api.spoonacular.com/recipes/search?query=burgers&apiKey=4cc34612813a4bafa176a17b31e1c6e1"
    # spoonacular_url = "https://api.spoonacular.com/recipes/search?query=burger&number=1"
    response = requests.get(spoonacular_url)
    json_body = response.json()
    
    # tweets = random.randint(0,8)
    #recipe name 
    recipe_title = json_body["results"][random_tweet]["title"]
    serving_size = json_body["results"][random_tweet]["servings"]
    recipe_image = str(json_body['results'][random_tweet]['image'])
    # recipe_image = json_body["results"][random_tweet]["image"]
    # #ingredients list 
    recipe_ingredients = json_body["results"][random_tweet]["id"]
 
    prep_time = json_body["results"][random_tweet]["readyInMinutes"]

    recipe_id = json_body["results"][random_tweet]["id"]
    burger_info = "https://api.spoonacular.com/recipes/{}/information?includeNutrition=false&apiKey=4cc34612813a4bafa176a17b31e1c6e1".format(recipe_id)
    response_2 = requests.get(burger_info)
    json_body_2 = response_2.json()
    burger_source_url = json_body_2["sourceUrl"]
    burger_pic = json_body_2["sourceUrl"]
 
    
    # return flask.render_template("index.html", recipe_title = recipe_title, servings_preptime= servings_preptime, recipe_image = recipe_image,recipe_ingredients= recipe_ingredients, recipe_link= recipe_link, tweets_about_burgers= tweets_about_burgers)
    return flask.render_template("index.html", recipe_title = recipe_title, burger_pic=burger_pic,
    serving_size= serving_size, prep_time= prep_time, 
    recipe_id = recipe_id,
    recipe_image = recipe_image,
    burger_source_url = burger_source_url,
    tweets_about_burgers= tweets_about_burgers)


    # return flask.render_template("index.html", burger_pic=burger_pic)
    
app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'))