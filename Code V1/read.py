from connection import getConnection

class Read:
    def func_ReadData(self):
        # Get the sql connection
        connection = getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute('Select * from record')

        # Print the data
        for row in cursor:
            print('row = %r' % (row,))