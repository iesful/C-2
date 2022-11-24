#when the menu is finished we should move everything into the faker_sql_main.py
#file so it can run along side all the other code in one go --Ivan

import sqlite3
con = sqlite3.connect("C^2.db")
cursor = con.cursor 

#options menu
def menu_print():
    menu = "\
        {:^24}  \n\n\
    |1. {:^24} |\n\
    |2. {:^24} |\n\
    |3. {:^24} |\n\
    |4. {:^24} |\n\
    |5. {:^24} |\n"

    print(menu.format('C^2 Database Menu', 'Add a new record', 'Modify a record',
    'Delete a record', 'View reports', 'Quit'))

menu_print()
#takes the user's choice from the menu options
action_choice = input("Please type the number infront of the action you would like to take: ")

leave = 'N'
while leave != "Y":

    #option 1 logic
    if action_choice == '1':
        prompt = input("You have selected to add a new record. Would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
        #list of tables available to add a record too
            tables = "\
                {:^24}  \n\n\
            |1. {:^24} |\n\
            |2. {:^24} |\n\
            |3. {:^24} |\n\
            |4. {:^24} |\n\
            |5. {:^24} |\n\
            |6. {:^24} |\n\
            |7. {:^24} |\n"

            print(tables.format('Tables', 'CUSTOMER_INFO', 'TEST_TAKER_INFO',
            'TESTING_CENTER_INFO', 'CERT_ORDERS', 'CERTIFICATION_INFO', 'JOB_INFO_OPPORTUNITIES','APPOINTMENTS' ))
            
        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")
        

    #option 2 logic
    if action_choice == '2':
        prompt = input("You have selected to modify a record. Would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            pass

        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

    #option 3 logic
    if action_choice == '3':
        prompt = input("You have selected to delete a record. Would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            pass

        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

    #option 4 logic
    if action_choice == '4':
        prompt = input("You have selected to view reports. Would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            pass
        
        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

        

    #option 5 logic
    if action_choice == '5':
        prompt = input("You have selected to exit the program would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            leave = prompt
            print("\n| {:^24} |".format('Exiting the C^2 Database Menu'))
        else:
            action_choice = input("Please type the number infront of the action you would like to take: ")
