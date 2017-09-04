import psycopg2

def cockroachdb(db, user, host, query):
    conn = psycopg2.connect(database=db , user=user, host=host, port=26257)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute(query)

    try:
        rows = cur.fetchall()
        log.logger.info('Initial balances:')

        for row in rows:
            log.logger.info([str(cell) for cell in row])
    except:
        print "Nothing to fetch"

    cur.close()
    conn.close()
