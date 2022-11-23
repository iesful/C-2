#when the menu is finished we should move everything into the faker_sql_main.py
#file so it can run along side all the other code in one go --Ivan

import sqlite3
con = sqlite3.connect("C^2.db")
cursor = con.cursor 

#options menu
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
        report_menu = "\n\
            {:^32}  \n\
        |1. {:^32} |\n\
        |2. {:^32} |\n\
        |3. {:^32} |\n\
        |4. {:^32} |\n\
        |5. {:^32} |\n\
        |6. {:^32} |\n\
        |7. {:^32} |\n\
        |8. {:^32} |\n\
        |9. {:^32} |\n\
        |10.{:^32} |\n\
        |11.{:^32} |\n"
        print(report_menu.format('Report Menu', '3 Most Expensive Certifications', 'Quickest Examinee', 'Number of Upcoming Appointments',
        'List of all Certifications', 'Highest Scoring Examinee', 'Favorite Testing Center', 'Top 3 Most Expensive Orders',
        'Most Positive Testing Date', 'List of all Jobs', 'Highest Paying Job', 'Return to Main Menu'))

        report_choice = input("Please select a report to generate: ")
        leave_report = 'N'
        while leave_report != 'Y':
            if report_choice == '1':
                data = cursor.execute("SELECT CERT_NAME, PRICE FROM CERTIFICATION_INFO").fetchall()
                top_3 = [0]
                for i in range(len(data)):
                    if data[i] not in top_3 and (data[i][1] > top_3[0]):
                        top_3.append(data[i])


            if report_choice == '2':
                pass

            if report_choice == '3':
                pass

            if report_choice == '4':
                pass

            if report_choice == '5':
                pass

            if report_choice == '6':
                pass

            if report_choice == '7':
                pass

            if report_choice == '8':
                pass

            if report_choice == '9':
                pass

            if report_choice == '10':
                pass

            if report_choice == '11':
                prompt = input("You have selected to exit the report menu would you like to continue (Y/N)? ").upper()
                if prompt == 'Y':
                    leave_report = prompt
                    action_choice = input("Please type the number infront of the action you would like to take: ")
                else:
                    report_choice = input("Please select a report to generate: ")


    #option 9 logic
    if action_choice == '9':
        prompt = input("You have selected to exit the program would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            leave = prompt
            print("\n| {:^24} |".format('Exiting the C^2 Database Menu'))
        else:
            action_choice = input("Please type the number infront of the action you would like to take: ")

