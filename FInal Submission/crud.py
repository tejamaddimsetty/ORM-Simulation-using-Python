# from prettytable import PrettyTable
from prettytable import PrettyTable
from connection import getConnection
from create import Create
from Update import Update
from Delete import Delete

class Read:
    rowl = []
    def outerFun(fnc):

        def innerFun(arg):
            print('\nSelect below option ::\n')
            print(
                f" 1.Read Students Details, \n 2.Add New Student, \n 3.Update Student, \n 4.Remove Student, \n 5.Exit \n")
            choice = input('Choose your option = ')

            if choice == '1':
                # readObj = Read( )
                # readObj.func_ReadData( )
                print('\nSelect below option ::\n')
                print(f" 1.Display in List Format, \n 2.Display in Table format, \n 3.Back to Previous Menus, \n")
                choice = input('Choose your option = ')

                if choice == '1':

                    fnc(arg)
                    print("-" * 40)
                    return


                elif choice == '2':
                    print("-" * 40)
                    fnc(arg)
                    print("-" * 40)
                    return

                elif choice == '3':
                    return
                else:
                    print('Wrong choice, You are going exist.')
                    print("-" * 40)

                print("-" * 40)

            elif choice == '2':
                createObj = Create( )               #created the object of the class Create
                createObj.func_CreateData( )        #calling function using object
                print("-" * 40)
                return

            elif choice == '3':
                updateObj = Update( )               #created the object of the class Update
                updateObj.func_UpdateData( )        #calling function using object
                print("-" * 40)
                return

            elif choice == '4':
                deleteObj = Delete( )               #created the object of the class Update
                deleteObj.func_DeleteData( )        #calling function using object
                print("-" * 40)
                return

            elif choice == '5':
                return
            else:
                print('Wrong choice, You are going exist.')
                print("-" * 40)




        return innerFun

    @outerFun
    def exratcdata(amt):
        # Get the sql connection
        connection = getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute('Select * from record')


        # Print the data
        for rowl in cursor:

           # print('row = %r' % (rowl,))
            print(list(rowl))

    @outerFun           #decorator
    def exratcdata1(amt):
        # Get the sql connection
        connection = getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute('Select * from record')


        # Print the data
        for rowl in cursor:
            x = PrettyTable(['ID', 'Name', 'Age', 'Class', 'School'])    #used pretty table to show the data in the table format

            x.add_row([rowl[0], rowl[1], rowl[2], rowl[3], rowl[4]])
            print(x)






    exratcdata(rowl)    #show in list
    exratcdata1(rowl)  #show in table


