import json
import datetime
import db_handler

def get():
    response = db_handler.cockroachdb(config.db["db"], config.db['user'], config.db['host'],
        "SELECT * FROM  deploy" )

    return json.loads(response)
