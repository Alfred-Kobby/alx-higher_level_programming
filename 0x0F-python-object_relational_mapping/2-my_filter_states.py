#!/usr/bin/python3
"""
author: Alfred Ternor
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    user_input = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data, port=3306)
    curs = db.cursor()
    num_rows = curs.execute("SELECT * FROM states WHERE states.name LIKE \
                           BINARY '{}' ORDER BY states.id;".format(user_input))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
