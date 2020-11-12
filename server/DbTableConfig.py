from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2

def create_tables(cur, DEBUG):
    cur.execute("select * from information_schema.tables where table_name=%s", ('humidity',))
    humidityTable = bool(cur.rowcount)

    if not humidityTable:
        if DEBUG:
            print("[INFO] - CREATING TABLE humidity")
        cur.execute('''CREATE TABLE humidity
            (
                VALUE           FLOAT           NOT NULL,
                TIMESTAMP       TIMESTAMP       NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - Humidity exists")

    cur.execute("select * from information_schema.tables where table_name=%s", ('particles',))
    particles = bool(cur.rowcount)

    if not particles:
        if DEBUG:
            print("[INFO] - CREATING TABLE particles")
        cur.execute('''CREATE TABLE particles
            (
                PM1            INTEGER          NOT NULL,
                PM10           INTEGER          NOT NULL,
                PM25           INTEGER          NOT NULL,
                TIMESTAMP      TIMESTAMP        NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - particles exists")

    cur.execute("select * from information_schema.tables where table_name=%s", ('pressure',))
    pressureTable = bool(cur.rowcount)

    if not pressureTable:
        if DEBUG:
            print("[INFO] - CREATING TABLE pressure")
        cur.execute('''CREATE TABLE pressure
            (
                VALUE           FLOAT           NOT NULL,
                TIMESTAMP       TIMESTAMP       NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - pressure exists")

    cur.execute("select * from information_schema.tables where table_name=%s", ('temperature',))
    temperatureTable = bool(cur.rowcount)

    if not temperatureTable:
        if DEBUG:
            print("[INFO] - CREATING TABLE temperature")
        cur.execute('''CREATE TABLE temperature
            (
                VALUE           FLOAT           NOT NULL,
                TIMESTAMP       TIMESTAMP       NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - Temperature exists")

    cur.execute("select * from information_schema.tables where table_name=%s", ('airquality',))
    airqualityTable = bool(cur.rowcount)

    if not airqualityTable:
        if DEBUG:
            print("[INFO] - CREATING TABLE airquality")
        cur.execute('''CREATE TABLE airquality
            (
                VALUE           FLOAT             NOT NULL,
                TIMESTAMP       TIMESTAMP       NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - Airquality exists")

    cur.execute("select * from information_schema.tables where table_name=%s", ('gps',))
    gpsTable = bool(cur.rowcount)

    if not gpsTable:
        if DEBUG:
            print("[INFO] - CREATING TABLE gps")
        cur.execute('''CREATE TABLE gps
            (
                TIMESTAMP       TIMESTAMP       NOT NULL,
                LAT             FLOAT           NOT NULL,
                LONG            FLOAT           NOT NULL,
                ALT             FLOAT           NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - GPS exists")

    cur.execute("select * from information_schema.tables where table_name=%s", ('light',))
    lightTable = bool(cur.rowcount)

    if not lightTable:
        if DEBUG:
            print("[INFO] - CREATING TABLE light")
        cur.execute('''CREATE TABLE light
            (
                VALUE           FLOAT           NOT NULL,
                TIMESTAMP       TIMESTAMP       NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - light exists")

    cur.execute("select * from information_schema.tables where table_name=%s", ('loudness',))
    loudnessTable = bool(cur.rowcount)

    if not loudnessTable:
        if DEBUG:
            print("[INFO] - CREATING TABLE loudness")
        cur.execute('''CREATE TABLE loudness
            (
                VALUE           FLOAT           NOT NULL,
                TIMESTAMP       TIMESTAMP       NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - loudness exists")

    cur.execute("select * from information_schema.tables where table_name=%s", ('motion',))
    motionTable = bool(cur.rowcount)

    if not motionTable:
        if DEBUG:
            print("[INFO] - CREATING TABLE motion")
        cur.execute('''CREATE TABLE motion
            (
                VALUE           FLOAT           NOT NULL,
                TIMESTAMP       TIMESTAMP       NOT NULL
            ); ''')
    else:
        if DEBUG:
            print("[INFO] - motion exists")

def create_database(DEBUG):
    con = psycopg2.connect(database="postgres", user="11800991", password="admin123", host="127.0.0.1", port="5432")
    print("[INFO] - Connected to DP Postgres.")
    cur = con.cursor()
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    cur.execute("SELECT datname FROM pg_database;")
    list_database = cur.fetchall()
    if ("att",) in list_database:
        if DEBUG:
            print("[INFO] - DB att exists")
        return
    else:
        if DEBUG:
            print("[INFO] - CREATING DATABASE ATT...")
        cur.execute('CREATE DATABASE ATT')
    con.close()