from connection import getConnection

class Delete:
    def func_DeleteData(self):
        # Get the SQL connection
        connection = getConnection()

        id = input('Enter record Id = ')

        try:
            # Get record which needs to be deleted
            sql = "Select * From record Where Id = %s"
            Id = id
            cursor = connection.cursor()
            cursor.execute(sql, [Id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', Id)
            print('ID\t\t Name\t\t\t Age')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm == 'Y' or 'y':
                deleteQuery = "Delete From record Where Id = %s"

                cursor.execute(deleteQuery, [Id])
                connection.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
                return confirm
        except:
            print('Something wrong, please check')
        finally:
            connection.close()