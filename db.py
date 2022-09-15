import sqlite3

from config import DB_PATH


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    return cursor


def push_and_close_connection(cursor, query):
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data


queries = {
    'query_title': """ SELECT "title", "country", max("release_year"), "listed_in", "description"
                       FROM netflix
                       WHERE title = '{}'
                    """,

    'query_release_year': """ SELECT "title", "release_year"
                              FROM netflix 
                              WHERE release_year BETWEEN '{}' AND '{}'
                              ORDER BY "release_year"
                              LIMIT 100
                           """,
    'query_rating': """ SELECT "title", "release_year", "rating"
                        FROM netflix 
                        WHERE rating IN {}
                    """,
    'query_genre': """ SELECT "title", "description"
                        FROM netflix
                        WHERE "listed_in" LIKE '{}'
                        ORDER BY release_year
                        LIMIT 10
                    """,
    'query_close_actors': """ SELECT "cast"
                              FROM netflix
                              WHERE "cast" LIKE '%{}%' AND "cast" LIKE '%{}%'
                          """,

    'query_movie_info': """ SELECT "title", "type", "release_year", "listed_in", "description"
                            FROM netflix
                            WHERE "type" = '{}' AND "release_year" = '{}' AND "listed_in" LIKE '{}%'
                        """
}
