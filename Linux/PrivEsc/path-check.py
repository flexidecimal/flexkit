import os

path = os.getenv('PATH')

dirs = path.split(':')

for directory in dirs:
    if os.access( directory, os.X_OK | os.W_OK ):
        print('User can write to: ' + directory)