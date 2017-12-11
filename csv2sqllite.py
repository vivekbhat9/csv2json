import csv
import sqlite3
import sys


def make_db_conn(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        #conn = sqlite3.connect(':memory:')
        # print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #    conn.close()

    return (conn)


def create_table(conn):
    sql = """ create table if not exists wine_data(
    id integer primary key,
    country text,
    description text,
    designation text,
    points text,
    price float,
    province text,
    region_1 text,
    region_2 text,
    taster_name text,
    taster_twitter text,
    title text,
    variety text,
    winery  text,
    flag integer
    )"""
    try:
        c = conn.cursor()
        c.execute(sql)
    except Exception as e:
        print(e)


# Main program starts here
db_file = sys.argv[1:][0]
csv_file = sys.argv[1:][1]
json_file = sys.argv[1:][2]

(conn) = make_db_conn(db_file)

create_table(conn)

dump_csv_sqlite()
