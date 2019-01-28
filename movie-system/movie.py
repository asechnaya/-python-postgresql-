'''
The Ctrl+Shift+J shortcut joins two lines into one and removes unnecessary spaces to match your code style.
'''
class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.director = 'Wachowski'
        self.watched = watched

    def __repr__(self):
        return '<movie {}>'.format(self.name)

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched

        }

