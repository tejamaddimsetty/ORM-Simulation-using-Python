from connection import getConnection


class Update:
    def func_UpdateData(self):
        # Get the SQL connection
        connection = getConnection()

        id = input('Enter record Id = ')

        try:
            # Fetch the data which needs to be updated
            sql = "Select * From record Where Id = %s"
            Id = id
            cursor = connection.cursor()
            cursor.execute(sql, [Id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', Id)
            print('ID\t\t Name\t\t\t Age\t\t\t Class\t\t\t School')
            print('---------------------------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2], item[3], item[4]))
            print('---------------------------------------------------------------')
            print('Enter New Data To Update Candidate Record ')

            name = input('Enter New Name = ')
            age = input('Enter New Age = ')
            clas = input('Enter Class = ')
            school = input('Enter School = ')
            query = "Update record Set Name = %s, Age = %s, Class = %s, School = %s Where Id = %s"
            val = (name, age, clas, school, id)
            # Execute the update query
            cursor.execute(query, val)
            connection.commit()
            print('Data Updated Successfully')

        except:
            print('Something wrong, please check')

        finally:
            # Close the connection
            connection.close()
