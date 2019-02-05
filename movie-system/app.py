# 100DaysOfCode, Day 13
import user
from movie import Movie

user = User('Jose')
user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The interview","Comedy")

user.save_to_file()
#print(user.watched_movies())


user = User.load_from_file('Jose.txt')

