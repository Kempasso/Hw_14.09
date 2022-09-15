import json

from db import get_connection, push_and_close_connection, queries


def format_to_dict(formatter, tuple_info):
    list_of_films = []
    for item in range(len(tuple_info)):
        adding_dict = dict(zip(formatter, tuple_info[item]))
        list_of_films.append(adding_dict)
    return list_of_films


def get_films_by_parameters(key, formatter, *args):
    cursor = get_connection()
    query = queries[key].format(*args)
    movie_info = push_and_close_connection(cursor, query)
    json_movie_info = format_to_dict(formatter, movie_info)
    return json_movie_info


def get_close_actors(key, first_actor, second_actor):
    cursor = get_connection()
    query = queries[key].format(first_actor, second_actor)
    all_casts = push_and_close_connection(cursor, query)
    counter = []
    for tuple_actors in all_casts:
        counter += tuple_actors[0].split(', ')
    close_actors = {k for k in counter if counter.count(k) > 2 and k not in (first_actor, second_actor)}
    return list(close_actors)


def get_json_movie_info(formatter, key, type_of, release_year, genre):
    cursor = get_connection()
    query = queries[key].format(type_of, release_year, genre)
    movie_info = push_and_close_connection(cursor, query)
    dict_movie_info = format_to_dict(formatter, movie_info)
    json_movie_info = json.dumps(dict_movie_info, ensure_ascii=False, indent=4)
    return json_movie_info
