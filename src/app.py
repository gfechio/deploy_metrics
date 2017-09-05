#!/usr/bin/python

import json
import datetime

from flask import Flask
from flask import request

import statistics
import config
import db_handler
import log

app = Flask(__name__)

@app.route("/deploy", methods=['GET', 'POST'])
def deploy():
    if request.method == 'POST':

        if request.headers['Content-Type'] == 'application/json':
            req = json.dumps(request.data)
            #XXX : FIX what is wrng here :
            for item in json.loads(req)[0]:
                data["id"] = item['id']
                data["status"] = item['status']

            date = datetime.datetime.today()
            data["time"] = date.strftime("%Y-%m-%d %H:%M:%S")
            db_handler.cockroachdb(config.db["db"], config.db['user'], config.db['host'],
                "INSERT INTO deploy (time, status, id) VALUES ('%s', %s, %s)"
                %(data['time'], data['status'],data['req']) )

            log.logger.info("request.response")
            return  "200 OK"
        else:
            return "Only JSON Supported so far...."

    elif request.method == 'GET':
        return statistics.get()


if __name__ == "__main__":
    app.run()

