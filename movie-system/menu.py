# 100DaysOfCode, Day 16
import json
import os

from user import User


def menu():
    name = input("Enter your name: ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

        user_input = input("Введите 'a', чтобы добавить фильм, "
           "'s' для списка фильмов, 'w', чтобы отметить просмотренное "
           "'d', чтобы удалить фильм, \n"
           "'l' - вывести список просмотренных фильмов "
           "'f' для сохранения и 'q' выхода\n")

    while user_input !='q':
        if user_input == 'a':
            movie_name = input('Введите название фильма: ')
            movie_genre = input('Введите жанр фильма: ')
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print('Название: {} Жанр: {} Просмотрено: {}'.format(movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input('Введит название фильма, чтобы пометить его как просмотренное')
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input('Введит название фильма для удаления')
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print('Название: {} Жанр: {} Просмотрено: {}'.format(movie.name, movie.genre, movie.watched))
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(),f)

        user_input = input("Введите 'a', чтобы добавить фильм, "
           "'s' для списка фильмов, 'w', чтобы отметить просмотренное "
           "'d', чтобы удалить фильм, \n"
           "'l' - вывести список просмотренных фильмов "
           "'f' для сохранения и 'q' выхода\n")


def file_exists(filename):
    return os.path.isfile(filename)

    
menu()
