from flask import Flask, jsonify

from config import FORMATTERS
from movie_blueprint.views import movie_blueprint
from rating_blueprint.views import rating_blueprint
from utils import get_close_actors, get_json_movie_info, get_films_by_parameters

app = Flask(__name__)

app.register_blueprint(movie_blueprint)
app.register_blueprint(rating_blueprint)


@app.route('/genre/<genre>')
def view_film_by_genre(genre):
    json_movie_info = get_films_by_parameters('query_genre', FORMATTERS['genre'], genre)
    return jsonify(json_movie_info)


get_close_actors('query_close_actors', 'Rose McIver', 'Ben Lamb')

get_json_movie_info(FORMATTERS['movie_info'], 'query_movie_info', 'Movie', 2020, 'Dramas')

app.run()
