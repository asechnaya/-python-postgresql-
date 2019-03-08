from user import User
"""
my_user = User('jose@schoolofcode.com', 'Jose', 'Salvatierra', None)
print(my_user)
my_user.save_to_db()
#-----
my_user = User.load_from_db_by_email('jose@schoolofcode.com')
print(my_user)

"""
my_user = User('rolf@rsmith.com', 'Rolf', 'Smith', None)
my_user.save_to_db()