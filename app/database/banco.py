import sqlite3
from sqlite3 import Error
import datetime
#create_db(physical, logical, boot, system, node, release, version, arch, processor):


def create_connection():
    #db_connection = None

    
    try:
        db_connection = sqlite3.connect("stats_db.db")
        return db_connection

    except Error as e:
        print (e)

    return db_connection



 
def create_table(db_connection):
    try:
        cursor = db_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS stats (counter int, physical text, logical text, boot text, system text, node text, release text, version text, arch text, proc text)")
    except Error as e:
        print(e)

def insert_table(db_connection, physical, logical, boot, system, node, release, version, arch, proc):
    try:
        c = db_connection.cursor()
        counter = count_rows(db_connection) + 1

        c.execute("insert into stats ( counter, physical, logical, boot, system, node, release, version, arch, proc) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" , ( counter, physical, logical, boot, system, node, release, version, arch, proc))

        db_connection.commit()
        return counter
    except Error as e:
        print(e)


def print_data(db_connection):
    #db_connection = sqlite3.connect("stats.db")
    cursor = db_connection.cursor()
    data =  cursor.execute("SELECT * FROM stats")
    for row in data:
        return (row)

def count_rows(db_connection):
    #db_connection = sqlite3.connect("stats.db")
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM stats")
    count = int(len(cursor.fetchall()))
    return(count)

#db_connection, counter = create_connection()
#print_data(db_connection)
#print (counter)