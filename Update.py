from connection import getConnection


class Update:
    def func_UpdateData(self):
        # Get the SQL connection
        connection = getConnection()

        id = input('Enter record Id = ')

        try:
            # Fetch the data which needs to be updated
            sql = "Select * From records Where Id = %s"
            Id = id
            cursor = connection.cursor()
            cursor.execute(sql, [Id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', Id)
            print('ID\t\t Name\t\t\t Age')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Enter New Data To Update Employee Record ')

            name = input('Enter New Name = ')
            age = input('Enter New Age = ')
            query = "Update records Set Name = %s, Age = %s Where Id = %s"
            val = (name, age, id)
            # Execute the update query
            cursor.execute(query, val)
            connection.commit()
            print('Data Updated Successfully')

        except:
            print('Something wrong, please check')

        finally:
            # Close the connection
            connection.close()