from flask import Blueprint, jsonify

from config import FORMATTERS
from utils import get_films_by_rating

rating_blueprint = Blueprint('rating', __name__, url_prefix='/rating')


@rating_blueprint.route('/children')  # (включаем сюда рейтинг G)
def view_children_films():
    children_rating = ('G', 'G')
    json_movie_info = get_films_by_rating('query_rating', FORMATTERS['rating']['children'], children_rating)
    return jsonify(json_movie_info)


@rating_blueprint.route('/family')  # (G, PG, PG-13)
def view_family_films():
    family_rating = ('G', 'PG', 'PG-13')
    json_movie_info = get_films_by_rating('query_rating', FORMATTERS['rating']['family'], family_rating)
    return jsonify(json_movie_info)


@rating_blueprint.route('/adult')  # (R, NC-17)
def view_adult_films():
    adult_rating = ('R', 'NC-17')
    json_movie_info = get_films_by_rating('query_rating', FORMATTERS['rating']['adult'], adult_rating)
    return jsonify(json_movie_info)
