import json
from collections import Counter

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


def get_close_actors(key, *actors):
    cursor = get_connection()
    query = queries[key]
    all_casts = push_and_close_connection(cursor, query)
    counter = []
    for tuple_actors in all_casts:
        list_actors = str(tuple_actors[0]).split(', ')
        if actors[0] in list_actors and actors[1] in list_actors:
            list_actors.remove(actors[0])
            list_actors.remove(actors[1])
            counter += list_actors
        else:
            continue
    dict_close_actors = dict(Counter(counter))
    close_actors = []
    for k in dict_close_actors.items():
        if k[1] > 2:
            close_actors.append(k[0])
    return close_actors


def get_json_movie_info(formatter, key, type_of, release_year, genre):
    cursor = get_connection()
    query = queries[key].format(type_of, release_year, genre)
    movie_info = push_and_close_connection(cursor, query)
    dict_movie_info = format_to_dict(formatter, movie_info)
    json_movie_info = json.dumps(dict_movie_info, ensure_ascii=False, indent=4)
    return json_movie_info
