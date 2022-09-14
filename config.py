DB_PATH = 'netflix.db'
FORMATTERS = {'title': ("title", "country", "release_year", "genre", "description"),
              'release': ("title", "release_year"),
              'genre': ("title", "description"),
              'movie_info': ("title", "type", "release_year", "listed_in", "description"),
              'rating':
                  {'children': ("title", "release_year", "rating"),
                   'family': ("title", "release_year", "rating"),
                   'adult': ("title", "release_year", "raiting")
                   }
              }
