import mysql.connector
from connection import getConnection


class Create:
    def func_CreateData(self):

        # Get the sql connection
        connection = getConnection()

        id = input('Enter Id = ')
        name = input('Enter Name = ')
        clas = input('Enter Class = ')
        age = input('Enter Age = ')
        school = input('Enter School = ')


        try:
            query = "INSERT INTO record(Id, Name, Class, Age, School) VALUES(%s, %s, %s, %s, %s)"
            VALUES = id, name, clas, age, school
            cursor = connection.cursor( )

            # Execute the sql query
            cursor.execute(query, VALUES)

            # Commit the data
            connection.commit( )
            print('Data Saved Successfully')
            print(id, name, clas, age, school)

        except:
            print('Something wrong, please check')


            connection.close( )
