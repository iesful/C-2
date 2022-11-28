#when the menu is finished we should move everything into the faker_sql_main.py
#file so it can run along side all the other code in one go --Ivan

import sqlite3, datetime
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

            print(tables.format('Tables', 'CUSTOMER_INFO','TESTING_CENTER_INFO',
             'CERT_ORDERS','TEST_TAKER_INFO', 'CERTIFICATION_INFO', 'JOB_INFO_OPPORTUNITIES','APPOINTMENTS' ))
            table_selection = input("Please enter the number of the table you would like to add a record to: ")
            if table_selection == "1":
                entered_name = input("Please input the name of the customer(First Last):")
                entered_street = input("Please enter the customer's street address:")
                entered_city = input("Please input the customer's city:")
                entered_state = input("Please input the customer's state abbreviation (TX):").upper
                entered_date = datetime.date.today()
                entered_TC_ID = input("Please enter the customer's preferred Testing Center ID (1-15):")
                entered_email = input("Please input the customer's email address:")
                #insert_into_customer_info(entered_name, entered_street, entered_city, entered_state, entered_date, entered_TC_ID, entered_email)
                print("Record added successfully...")
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")

            if table_selection == "2":
                enterer_tc_name = input("Please input the name of the testing center:")
                
            if table_selection == "3":
                pass
            if table_selection == "4":
                pass
            if table_selection == "5":
                pass
            if table_selection == "6":
                pass
            if table_selection == "7":
                pass
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
        print(report_menu.format('Report Menu', 'Most Expensive Certifications', 'Quickest Examinee', 'Number of Upcoming Appointments',
        'List of all Certifications', 'Highest Scoring Examinee', 'Favorite Testing Center', 'Top 3 Most Expensive Orders',
        'Most Positive Testing Date', 'List of all Jobs', 'Highest Paying Job', 'Return to Main Menu'))

        report_choice = input("Please select a report to generate: ")
        leave_report = 'N'
        while leave_report != 'Y':
            if report_choice == '1':
                data = cursor.execute("SELECT CERT_NAME, PRICE FROM CERTIFICATION_INFO").fetchall()
                top = [('A+', 246)]
                for i in range(len(data)):
                    if data[i] not in top and (data[i][1] > top[0][1]):
                        top.clear()
                        top.append(data[i])

                print(f"\nMost Expensive Certification: {top[0][0]}, Price: ${top[0][1]}\n")

                leave_report = 'Y'
                menu_print()
                action_choice = input("\nReturning to main menu\nPlease type the number infront of the action you would like to take: ")


            if report_choice == '2':
                data = cursor.execute("SELECT CUSTOMER_ID, TIME_USED FROM TEST_TAKER_INFO").fetchall()
                to_sort = []
                for i in range(len(data)):
                    to_sort.append([data[i][0], int(data[i][1])])

                to_sort.sort(key=lambda x: int(x[1]))

                customer_data = cursor.execute("SELECT CUSTOMER_ID, NAME FROM CUSTOMER_INFO").fetchall()
                for p in range(len(to_sort)):
                    for k in range(len(customer_data)):
                        if to_sort[p][0] == customer_data[k][0]:
                            to_sort[p][0] = customer_data[k][1]

                print(f"\nQuickest Examinee: {to_sort[0][0]} with a time of {to_sort[0][1]} minutes!\n")

                leave_report = 'Y'
                menu_print()
                action_choice = input("\nReturning to main menu\nPlease type the number infront of the action you would like to take: ")


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
                    menu_print()
                    action_choice = input("Please type the number infront of the action you would like to take: ")
                else:
                    report_choice = input("Please select a report to generate: ")
        
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
            menu_print
            action_choice = input("Please type the number infront of the action you would like to take: ")

    else:
        print ("Selection invalid. Please enter an appropriate selection...")
        menu_print()
        action_choice = input("Please type the number infront of the action you would like to take: ")
        



#will begin coding the rest of the menu on the faker_sql_main.py file as of 11/25/22 -Tim
