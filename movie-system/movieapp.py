# 100DaysOfCode, Day 14
from user import User
import json
#from movie import Movie


user = User('Jose')
user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The interview","Comedy")

with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)

#user.save_to_file()
#print(user.watched_movies())

'''
user = User.load_from_file('Jose.txt')
'''
print(user.json())

