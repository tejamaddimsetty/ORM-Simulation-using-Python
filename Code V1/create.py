import mysql.connector
from connection import getConnection


class Create:
    def func_CreateData(self):

        # Get the sql connection
        connection = getConnection()

        id = input('Enter Id = ')
        name = input('Enter Name = ')
        age = input('Enter Age = ')


        try:
            query = "INSERT INTO records(Id, Name, Age) VALUES(%s, %s, %s)"
            VALUES = id, name, age
            cursor = connection.cursor( )

            # Execute the sql query
            cursor.execute(query, VALUES)

            # Commit the data
            connection.commit( )
            print('Data Saved Successfully')
            print(id, name, age)

        except:
            print('Something wrong, please check')


            connection.close( )
