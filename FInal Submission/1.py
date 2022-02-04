
#Read, Create, Update, Delete these all are the classes imported here
from read import Read
from create import Create
from Update import Update
from Delete import Delete


def main():
    print('\nSelect below option ::\n')
    print(f" 1.Read Students Details, \n 2.Add New Student, \n 3.Update Student, \n 4.Remove Student, \n 5.Exit \n")
    choice = input('Choose your option = ')

    if choice == '1':
        readObj = Read( )          #created the object of the class Read
        readObj.func_ReadData( )   #using Object called the function
        print("-" * 40)
        return main()
    elif choice == '2':
        createObj = Create( )
        createObj.func_CreateData( )
        print("-" * 40)
        return main( )
    elif choice == '3':
        updateObj = Update()
        updateObj.func_UpdateData()
        print("-" * 40)
        return main( )
    elif choice == '4':
        deleteObj = Delete()
        deleteObj.func_DeleteData()
        print("-" * 40)
        return main( )
    elif choice == '5':
        return
    else:
        print('Wrong choice, You are going exist.')
        print("-" * 40)
        return main( )

# Call the main function
main()