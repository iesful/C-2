#text based menu to connect and interact with our database
import sqlite3
connection = sqlite3.connect("C^2.db")
crusor = connection.cursor

print ("\
| C^2 Database Menu |\n\n\
1. Create a new Table\n\
2. Drop a table\n\
3. Alter a table\n\
4. Update a table\n\
5. Insert into a table\n\
6. Delete from a table\n\
7. Search for a record in a table\n\
8. View reports\n\
9. Quit\n")

#takes the user's choice from the above options
ActionChoice = input("Please type the number infront of the action you would like to take: ")
leave = 'N'
while leave != "Y":

    if ActionChoice == 1:
        cancelChoice = input("You have selected to create a new table would you like to continue (Y/N)? ")
        if cancelChoice.upper == "Y":
            #the name you want to give the table 
            userTableName = input("Please enter the name you would like to give the new table: ")
            #the fields you want to include in the table
            newTableFieldName = input("Please input the names of the fields you want in your table separated by commas: ")
            #sql statment to add the table to the database goes here
        else:
            ActionChoice = input("Please type the number infront of the action you would like to take: ")

    if ActionChoice == 2:
        cancelChoice = input("You have selected to drop a table would you like to continue (Y/N)? ")
        if cancelChoice.upper == "Y":
            #the name of the table you would like to drop from the database
            userTableDropChoice = input("Please enter the name of the table you would like to drop: ")
            #sql to drop the table from the database goes here
        else:
            ActionChoice = input("Please type the number infront of the action you would like to take: ")

    #option 9 logic
    if ActionChoice == '9':
        cancelChoice = input("You have selected to exit the program would you like to continue (Y/N)? ").upper()
        if cancelChoice == "Y":
            leave = cancelChoice
            print("\n| Exiting the C^2 Database Menu |")
        else:
            ActionChoice = input("Please type the number infront of the action you would like to take: ")


    #continue the if statements until all menu options are covered
