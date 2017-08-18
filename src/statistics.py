import json
import datetime

def get():
    f = open('FILE.TXT', 'r')
    response = f.read(1)
    return "%s \n" %response
