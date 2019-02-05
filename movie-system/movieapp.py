# 100DaysOfCode, Day 14
from user import User
import json
#from movie import Movie

'''
user = User('Jose')
user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The interview","Comedy")

with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)
'''
with open('my_file.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)

print(user.json())

