#!/usr/bin/python3
'''takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument. '''
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    match_name = sys.argv[4].split(';')[0].strip("'")

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY \
                '{}'".format(match_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
