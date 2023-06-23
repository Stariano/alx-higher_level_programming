#!/usr/bin/python3
"""
List all cities from a database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, state.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id;")

    joined = cur.fetchall()
    for join in joined:
        print(join)
