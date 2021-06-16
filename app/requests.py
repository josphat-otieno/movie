import urllib.request,json
from .models import Movie




# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_movie(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movie_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movie_url) as url:
        get_movies_data = url.read()
        get_movies_data = json.loads(get_movies_data)

        movie_results = None
    
    return movie_results