from flask import Flask, jsonify

from utils import get_films_by_title_or_release, get_films_by_rating, get_films_by_genre, get_close_actors, \
    get_json_movie_info

app = Flask(__name__)

formatters = {'title': ("title", "country", "release_year", "genre", "description"),
              'release': ("title", "release_year"),
              'genre': ("title", "description"),
              'movie_info': ("title", "type", "release_year", "listed_in", "description"),
              'rating':
                  {'children': ("title", "release_year", "rating"),
                   'family': ("title", "release_year", "rating"),
                   'adult': ("title", "release_year", "raiting")
                   }
              }


@app.route('/movie/<title>')
def view_film_info(title):
    json_movie_info = get_films_by_title_or_release('query_title', formatters['title'], title)
    return jsonify(json_movie_info)


@app.route('/movie/<int:first_year>/to/<int:second_year>')
def view_film_by_release(first_year, second_year):
    json_movie_info = get_films_by_title_or_release('query_release_year', formatters['release'], first_year,
                                                    second_year)
    return jsonify(json_movie_info)


@app.route('/rating/children')  # (включаем сюда рейтинг G)
def view_children_films():
    children_rating = ('G', 'G')
    json_movie_info = get_films_by_rating('query_rating', formatters['rating']['children'], children_rating)
    return jsonify(json_movie_info)


@app.route('/rating/family')  # (G, PG, PG-13)
def view_family_films():
    family_rating = ('G', 'PG', 'PG-13')
    json_movie_info = get_films_by_rating('query_rating', formatters['rating']['family'], family_rating)
    return jsonify(json_movie_info)


@app.route('/rating/adult')  # (R, NC-17)
def view_adult_films():
    adult_rating = ('R', 'NC-17')
    json_movie_info = get_films_by_rating('query_rating', formatters['rating']['adult'], adult_rating)
    return jsonify(json_movie_info)


@app.route('/genre/<genre>')
def view_film_by_genre(genre):
    json_movie_info = get_films_by_genre('query_genre', formatters['genre'], genre)
    return jsonify(json_movie_info)


get_close_actors('query_close_actors', 'Rose McIver', 'Ben Lamb')
print(get_json_movie_info(formatters['movie_info'], 'query_movie_info', 'Movie', 2020, 'Dramas'))

app.run()
