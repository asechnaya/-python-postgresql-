from database import connect
class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name =last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with connect() as connection:
            with connection.cursor() as cursor:
                #running some code
                cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                               (self.email, self.first_name, self.last_name))
    @classmethod
    def load_from_db_by_email(cls, email):
        #another_user = cls('rolf@schoolofcode.com', 'Rolf', 'Smith', None)
        with connect() as connection:
            with connection.cursor() as cursor:
                #running some code
                cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
                user_data = cursor.fetchone()
                return cls(email=user_data[1], first_name=[2], last_name=[3], id=[0])
