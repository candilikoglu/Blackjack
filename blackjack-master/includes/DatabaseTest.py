#Database Reader

import sqlite3
from common import *

def databaseconnect(test1, test2):


    try:
        sqliteConnection = sqlite3.connect('StrategyDB.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)


        cursor.execute("select "+test1+" from scard where phand = '"+test2+"'")
        record2 = cursor.fetchall()
        item = record2[0][0]
        print("This command works and the item is: ", item)
        cursor.close()

    except sqlite3.Error as error:

        print("Error while connecting to sqlite", error)

    finally:

        if sqliteConnection:

            sqliteConnection.close()
            print("The SQLite connection is closed")

def main():

    print("This is a database test")

    databaseconnect("seven", "17")

if __name__=="__main__":

    main()
