#when the menu is finished we should move everything into the faker_sql_main.py
#file so it can run along side all the other code in one go --Ivan

#text based menu to connect and interact with our database
""" import sqlite3
connection = sqlite3.connect("C^2.db")
cursor = connection.cursor """

menu = "\
    {:^24}  \n\n\
|1. {:^24} |\n\
|2. {:^24} |\n\
|3. {:^24} |\n\
|4. {:^24} |\n\
|5. {:^24} |\n\
|6. {:^24} |\n\
|7. {:^24} |\n\
|8. {:^24} |\n\
|9. {:^24} |\n"
print(menu.format('C^2 Database Menu', 'Create a new Table', 'Drop a table',
'Alter a table', 'Update records', 'Insert records', 'Delete from a table',
'Search for records', 'View reports', 'Quit'))

""" print ("\
| C^2 Database Menu |\n\n\
| 1. Create a new Table |\n\
| 2. Drop a table |\n\
| 3. Alter a table |\n\
| 4. Update a table |\n\
| 5. Insert into a table |\n\
| 6. Delete from a table |\n\
| 7. Search for a record in a table |\n\
| 8. View reports |\n\
| 9. Quit |\n") """

#takes the user's choice from the above options
action_choice = input("Please type the number infront of the action you would like to take: ")

leave = 'N'
while leave != "Y":

    #option 1 logic
    if action_choice == '1':
        prompt = input("You have selected to create a new table would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            #the name you want to give the table 
            userTableName = input("Please enter the name you would like to give the new table: ")
            #the fields you want to include in the table
            newTableFieldName = input("Please input the names of the fields you want in your table separated by commas: ")
            #sql statment to add the table to the database goes here
        else:
            action_choice = input("Please type the number infront of the action you would like to take: ")

    #option 2 logic
    if action_choice == '2':
        prompt = input("You have selected to drop a table would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            #the name of the table you would like to drop from the database
            userTableDropChoice = input("Please enter the name of the table you would like to drop: ")
            #sql to drop the table from the database goes here
        else:
            action_choice = input("Please type the number infront of the action you would like to take: ")

    #option 3 logic
    if action_choice == '3':
        pass

    #option 4 logic
    if action_choice == '4':
        pass

    #option 5 logic
    if action_choice == '5':
        pass

    #option 6 logic
    if action_choice == '6':
        pass

    #option 7 logic
    if action_choice == '7':
        pass

    #option 8 logic
    if action_choice == '8':
        pass

    #option 9 logic
    if action_choice == '9':
        prompt = input("You have selected to exit the program would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            leave = prompt
            print("\n| {:^24} |".format('Exiting the C^2 Database Menu'))
        else:
            action_choice = input("Please type the number infront of the action you would like to take: ")


    #continue the if statements until all menu options are covered
