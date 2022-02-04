# import pypyodbc
# import config
import mysql.connector


# Return the sql connection


def getConnection():
    connection = mysql.connector.connect(user='root', password='root', host='localhost', database='stud')
    cursor = connection.cursor( )

    cursor.execute("SELECT DATABASE()")

    data = cursor.fetchone( )
    print("Connection established to: ", data)

    # cursor.execute("Show tables;")

    myresult = cursor.fetchall( )

    for x in myresult:
        print(x)

    return connection
