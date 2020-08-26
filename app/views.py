from flask import render_template
from app import app
from .request import get_movies

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to the best Movie Review Website Online'
    message = "Hello world"
    return render_template('index.html', message = message, title=title,popular = popular_movies )

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details and its data.
    '''

    return render_template('movie.html', id=movie_id)