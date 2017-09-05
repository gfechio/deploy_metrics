#!/usr/bin/python
import os
import config
import db_handler
import log

def create_db():

    if os.path.isfile("/src/db_done"):
        print "DB created"
    else:
        try:
            db_handler.cockroachdb("", "root", config.db['host'],
                "CREATE DATABASE %s" %(config.db['db']) )
            db_handler.cockroachdb(config.db["db"], config.db['user'], config.db['host'],
                "CREATE TABLE IF NOT EXISTS %s ( id INT PRIMARY KEY,  status VARCHAR, time TIMESTAMP )" %(config.db['db']) )
            f= open("/src/db_done","w+")
            f.close()
        except:
            db_handler.cockroachdb(config.db["db"], "root", config.db['host'],
                "CREATE TABLE IF NOT EXISTS %s ( id INT PRIMARY KEY,  status VARCHAR, time TIMESTAMP )" %(config.db['db']) )
            print "DB Created"

        db_handler.cockroachdb(config.db["db"], "root", config.db['host'],
            "GRANT ALL ON DATABASE deploy TO %s" %(config.db['user']) )
        db_handler.cockroachdb(config.db["db"], "root", config.db['host'],
            "GRANT INSERT ON TABLE deploy TO %s" %(config.db['user']) )
        db_handler.cockroachdb(config.db["db"], "root", config.db['host'],
            "GRANT UPDATE ON TABLE deploy TO %s" %(config.db['user']) )
        db_handler.cockroachdb(config.db["db"], "root", config.db['host'],
            "GRANT DELETE ON TABLE deploy TO %s" %(config.db['user']) )
    return "DB created" 



create_db()

