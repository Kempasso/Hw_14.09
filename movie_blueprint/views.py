from flask import Blueprint, jsonify

from config import FORMATTERS
from utils import get_films_by_parameters

movie_blueprint = Blueprint('movie', __name__, url_prefix='/movie')


@movie_blueprint.route('/<title>')
def view_film_info(title):
    json_movie_info = get_films_by_parameters('query_title', FORMATTERS['title'], title)
    return jsonify(json_movie_info)


@movie_blueprint.route('/<int:first_year>/to/<int:second_year>')
def view_film_by_release(first_year, second_year):
    json_movie_info = get_films_by_parameters('query_release_year', FORMATTERS['release'], first_year,
                                              second_year)
    return jsonify(json_movie_info)
