#!/usr/bin/python

import json
import datetime

from flask import Flask
from flask import request

import load_file
import statistics
import log

app = Flask(__name__)

@app.route("/deploy", methods=['GET', 'POST'])
def deploy():
    if request.method == 'POST':    

        if request.headers['Content-Type'] == 'application/json':
            data = {}
            data["req"] = json.loads(request.data)
            date = datetime.datetime.today()
            data["time"] = date.strftime("%Y/%m/%d %H:%M:%S")
            load_file.write(data)
            log.logger.info("request.response") 
            return  "200 OK"
        else:
            return "Only JSON Supported so far...."

    elif request.method == 'GET':
        return statistics.get()


if __name__ == "__main__":
    app.run()
