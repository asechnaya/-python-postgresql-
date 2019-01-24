# 100DaysOfCode, Day 13
from movie import Movie
import user

user = User("Jose")

my_movie = Movie("The Matrix", "Sci-Fi", True)

user.movies.append(my_movie)

print(user)
print(user.watched_movies())
