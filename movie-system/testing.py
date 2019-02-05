import user from User
import json
with open('my_file.txt', 'w') as f:

    f.write('Hello, World!')

with open('my_file.txt', 'r') as f:
    print(f.readline())

with open('my_file.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)


'''
import sys
my_vars = []
for i in range(3):
    my_vars.append(lambda: i)
    print([f() for f in my_vars])
print(sys.argv)

'''