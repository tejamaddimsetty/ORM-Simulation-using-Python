from connection import getConnection
from prettytable import PrettyTable

class Read:
    def func_ReadData(self):
        # Get the sql connection
        connection = getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute('Select * from record')

        # Print the data

        #stud = PrettyTable(['ID','Name', 'Class', 'School', 'Age'])

        for row in cursor:
            #print('row = %r' % (row,))

            print(list(row))
