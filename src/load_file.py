import json

def write(string):
    with open('FILE.TXT', 'w') as f:
        f.write(str(string))
