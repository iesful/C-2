import sqlite3, datetime
from data_generator import *

cursor = sqlite3.connect('C^2.db')
cursor = cursor.cursor()

#options menu

#prints options menu
def menu_print():
    menu = "\
        {:^24}  \n\n\
    |0. {:^24} |\n\
    |1. {:^24} |\n\
    |2. {:^24} |\n\
    |3. {:^24} |\n\
    |4. {:^24} |\n\
    |5. {:^24} |\n\
    |6. {:^24} |\n"

    print(menu.format('C^2 Database Menu', 'View records', 'Add a new record', 'Modify a record',
    'Delete a record', 'Search for a record', 'View reports', 'Quit'))

menu_print()

#takes the user's choice from the menu options
action_choice = input("Please type the number infront of the action you would like to take: ")

leave = 'N'
while leave != "Y":
    #option 0 logic
    if action_choice == '0':
        prompt = input("You have selected to view records. Would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            
        #list of tables available to view records of CUSTOMER_INFO
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
            
            table_selection = input("Please enter the number of the table you would like to view to (e.g.: 1 - 7): ")
            print()
            if table_selection == "1":
                print("Displaying CUSTOMER_INFO Table Records:")
                print()
                cursor.execute("SELECT * FROM CUSTOMER_INFO")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x, '\n')
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
                
            if table_selection == "2":
                print("Displaying TESTING_CENTER_INFO Table Records:")
                print()
                cursor.execute("SELECT * FROM TESTING_CENTER_INFO")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x, '\n')
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
            
            if table_selection == "3":
                print("Displaying CERT_ORDERS Table Records:")
                print()
                cursor.execute("SELECT * FROM CERT_ORDERS")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x, '\n')
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
            
            if table_selection == "4":
                print("Displaying TEST_TAKER_INFO Table Records:")
                print()
                cursor.execute("SELECT * FROM TTEST_TAKER_INFO")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x, '\n')
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
                
            if table_selection == "5":
                print("Displaying CERTIFICATION_INFO Table Records:")
                print()
                cursor.execute("SELECT * FROM CERTIFICATION_INFO")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x, '\n')
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
                
            if table_selection == "6":
                print("Displaying JOB_INFO_OPPORTUNITIES Table Records:")
                print()
                cursor.execute("SELECT * FROM JOB_INFO_OPPORTUNITIES")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x, '\n')
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
            
            if table_selection == "7":
                print("Displaying APPOINTMENT Table Records:")
                print()
                cursor.execute("SELECT * FROM APPOINTMENTS")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x, '\n')
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
            
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

            table_selection = input("Please enter the number of the table you would like to add a record to (e.g.: 1 - 7): ")

            #if the user decides to add to customer_info table
            if table_selection == "1":

                #all the fields that need to be populated to create a record in the customer_info table
                entered_name = input("Please input the name of the customer (e.g: Firstname Lastname): ")
                entered_street = input("Please enter the customer's street address (e.g: 1234 Main Street): ")
                entered_city = input("Please input the customer's city (e.g: Houston): ")
                entered_state = input("Please input the customer's state abbreviation (e.g: TX): ").upper()
                entered_date = datetime.date.today()
                entered_TC_ID = input("Please enter the customer's preferred Testing Center ID (Pick from 1 - 15): ")
                entered_email = input("Please input the customer's email address (e.g.: BobSmith@gmail.com): ")

                #use the same function created at the beginning to insert into the customer_info table 
                insert_into_customer_info(entered_name, entered_street, entered_city, entered_state, entered_date, entered_TC_ID, entered_email)
                
                #commit statemtent so the db is updated as soon as you finish entering the data
                cursor.connection.commit()
                print("Returning to main menu...")
                
            #if the user decides to add to the testing_center_info table
            if table_selection == "2":
                ##all the fields that need to be populated to create a record in the testing_center_info table
                entered_tc_name = input("Please input the name of the testing center (e.g.: Webster TC): ")
                entered_tc_street = input("Please input the testing center's street address (e.g: 1234 Main Street): ")
                entered_city = input("Please input the customer's city (e.g: Houston): ")
                entered_tc_city = input("Please input the testing center's city (e.g: Houston): ")
                entered_tc_state = input("Please input the testing center's state abbreviation (e.g.: TX): ").upper()
                entered_tc_zip = input("Please input the testing centere's zip code (5 digit from e.g.: 77509): ")
                entered_tc_hours = "M - F, 9AM - 5PM"
                entered_email = input("Please input the customer's email address (e.g.: BobSmith@gmail.com): ")
                
                #use the function to insert into testing_center_info table
                
                insert_into_testing_center_info(entered_tc_name, entered_tc_street, entered_tc_city, entered_tc_state, entered_tc_zip)
                #commit statemtent so the db is updated as soon as you finish entering the data
                cursor.connection.commit()
                print("Returning to main menu...")
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")

            #if the user decides to add to the cert_orders table
            if table_selection == "3":
                #all the fields that need to be populated to create a record in the cert_orders table
                entered_cust_ID = input("Please enter the customer ID of the customer making the order: ")
                entered_cert_ID = input("Please enter the cert ID for the certification being ordered: ")
                entered_order_date = datetime.date.today()
                entered_order_cost = input("Please enter the cost of the cert being ordered:")
                #use the function to inser tinto the cert_orders table
                insert_into_cert_orders(entered_cust_ID, entered_cert_ID, entered_order_date, entered_order_cost)
                #commit statement so the db i supdated as soon as you finish entering the data
                cursor.connection.commit()
                print("Returning to main menu...")
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
                
            #if a user decides to add to the test_taker_info table
            if table_selection == "4":
                entered_exam_id = input("Please enter the exam id you'd like to add: ")
                entered_cust_id = input("Please enter the customer ID of the customer making the order: ")
                entered_cert_id = input("Please enter the cert ID for the certification being ordered: ")
                entered_tc_id = input("Please enter the name of the testing center ID you'd like to add: ")
                entered_actual_score = input("Please enter the value of the actual score you'd like to add: ")
                entered_time_used = input("Please enter the amount of time spent on this exam: ")
                entered_date_taken = input("Please enter the date in which you'd like to add: ")
                insert_into_test_taker_info(entered_exam_id, entered_cust_id, entered_cert_id, entered_tc_id, entered_actual_score, entered_time_used, entered_date_taken)
                cursor.connection.commit()
                print("Returning to main menu...")
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
                
            #if a user decides to add to the certification_info table
            if table_selection == "5":
                entered_cert_id = input("Please enter the cert ID for the certification being ordered: ")
                entered_cert_name = input("Please enter the name of the certificaiton you'd like to add: ")
                entered_exam_code = input("Please enter the exam code you'd like to add: ")
                entered_price = input("Please enter the price of the exam you'd like to add: ")
                entered_test_duration = input("Please enter the duration of the exam you'd like to add: ")
                entered_passing_score = input("Please enter the passing score of the exam you'd like to add: ")
                entered_number_of_questions = input("Please enter the value of the number of questions your exam has: ")
                insert_into_certification_info = (entered_cert_id, entered_cert_name, entered_exam_code, entered_price, entered_test_duration, entered_passing_score, entered_number_of_questions)
                print("Returning to main menu...")
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
                
            #if the user decides to add to the job_info_opportunities table
            if table_selection == "6":
                entered_job_id = input("Please enter the job ID relevant to the certification: ")
                entered_job_title = input("Please enter the job title relevant to the certification: ")
                entered_salary = input("Please enter the salary the individual may earn: ")
                entered_cert_id = input("Please enter the cert ID for the associated certification: ")
                insert_into_job_opportunities_table(entered_job_id, entered_job_title, entered_salary, entered_cert_id)
                print("Returning to main menu...")
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
            #if the user decides to add to the appointments table
            if table_selection == "7":
                #all the fields that need to be populated to create a record in the appointments table
                entered_cust_ID = input("Please input the ID number of the cusotmer the appointment is for: ")
                entered_TC_ID= input("Please input ID number of the testing center the appointment is at: ")
                entered_cert_ID = input("Please input the ID of the cert exam being taken: ")
                entered_app_date = input("Please input the date the appointment is for in YYYY-MM-DD format: ")
                #use the function to insert into appointments table
                insert_into_appointments(entered_cust_ID, entered_TC_ID, entered_cert_ID, entered_app_date)                
                #commit statemtent so the db is updated as soon as you finish entering the data
                cursor.connection.commit()
                print("Returning to main menu...")
                
                menu_print()
                action_choice = input("Please type the number infront of the action you would like to take: ")
        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")      

    #option 2 logic
    if action_choice == '2':
        prompt = input("You have selected to modify a record. Would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            #list of the tables available to modify a record in
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
            table_selection = input("Please enter the number of the table containing the record you want to modify:")
            #if the user decides to modify a record in the customer_info table
            if table_selection == "1":
                #sql update query for the customer_info table
                customer_info_sql_update = "UPDATE CUSTOMER_INFO\
                    SET NAME = ?, STREET = ?, CITY = ?, STATE = ?, SIGNUP_DATE = ?, TC_ID =?, EMAIL =?\
                    WHERE CUSTOMER_ID = ?"
                #included every field in the table so that one update query could be used to update 
                #any portion of the record
                #if you only need to update a certain field then just enter the same information
                # already in the db for fields that don't need to be updated
                cust_ID = input("Please input the ID number of the customer you want to update: ")
                name = input('Please input the name of the cusomer: ')
                street = input("Please enter the customer's street address: ")
                city = input("Please input the customer's city: ")
                state = input("Please input the customer's state abbreviation (TX): ").upper()
                date = input("Please input the date of the customer's account creation using the YYYY-MM-DD format: ")
                new_TC_ID = input("Please enter the customer's preferred Testing Center ID (1-15): ")
                email = input("Please input the customer's email address: ")
                
                
                user_input = (name, street, city, state, date, new_TC_ID, email, cust_ID)
                #executes the sql query using the users inputs
                cursor.execute(customer_info_sql_update, user_input)
                #commit statment to update the db as soon as the user finishes updating the data
                cursor.connection.commit()
                print("Customer updated successfully...")
            #if the user decides to modify a record in the testing_center_info table
            if table_selection == "2":
                 #sql update query for the testing_center_info table
                testing_center_sql_update = "UPDATE TESTING_CENTER_INFO\
                        SET TC_NAME = ?, STREET = ?, CITY = ?, STATE = ?, ZIP = ?, HOURS =?\
                        WHERE TC_ID = ?"
                #included every field in the table so that one update query could be used to update 
                #any portion of the record
                #if you only need to update a certain field then just enter the same information 
                #already in the db for fields that don't need to be updated
                tc_id = input("Please input the ID number of the testing center you want to update: ")
                tc_name = input("Please input the name of the testing center: ")
                street = input("Please input the testing center's street address: ")
                city = input("Please input the testing center's city: ")
                state = input("Please input the testing center's state: ")
                zip = input("Please input the testing centere's zip code(5 digit): ")
                hours = input("Please input the hours of opperation for this testing center following this format (M - F, 9AM - 5PM) ")
                user_input = (tc_name, street, city, state, zip, hours, tc_id)
                #executes the sql query using the users inputs
                cursor.execute(testing_center_sql_update, user_input)
                #commit statment to update the db as soon as the user finishes updating the data
                cursor.connection.commit()
                print("Testing Center updated successfully...")
            #if the user decides to update a record in the cert_orders table
            if table_selection == "3":
                #sql update query for the cert-orders table
                cert_orders_sql_update = "UPDATE CERT_ORDERS\
                    SET CUSTOMER_ID = ?, CERT_ID = ?, ORDER_DATE =?, ORDER_COST = ?\
                    WHERE ORDER_ID = ?"
                #included every field in the table so that one update query could be used to update 
                #any portion of the record
                #if you only need to update a certain field then just enter the same information 
                #already in the db for fields that don't need to be updated
                order_id = input("Please input the ID number of the order you want to update: ")
                customer_id = input("Please input the ID number of the customer who made the order: ")
                cert_id = input("Please input the ID number of the cert being ordered: ")
                order_date = input("Please input the date of the order using the YYYY-MM-DD format: ")
                order_cost = input("Please input the ordercost according to the cert ordered: ")
                user_input = (customer_id, cert_id, order_date, order_cost, order_id)
                #executes the sql query using the users inputs
                cursor.execute(cert_orders_sql_update, user_input)
                #commit statment to update the db as soon as the user finishes updating the data
                cursor.connection.commit()
                print("Order updated successfully")

            if table_selection == "4":
                pass
            if table_selection == "5":
                pass
            if table_selection == "6":
                pass
            if table_selection == "7":
                #sql update query for the appointments table
                app_sql_update = "UPDATE APPOINTMENTS\
                    SET CUSTOMER_ID = ?, TC_ID = ?, CERT_ID=?, APP_DATE = ?\
                    WHERE APP_ID = ?"
                #included every field in the table so that one update query could be used to update 
                #any portion of the record
                #if you only need to update a certain field then just enter the same information 
                #already in the db for fields that don't need to be updated
                app_id = input("Please input the ID number of the appointment you want to update: ")
                customer_id = input("Please input the ID number of the customer the appointment is for: ")
                app_tc_id = input("Please input the ID number of the testing center the appointment is at: ")
                cert_id = input("Please input the ID number of the cert exam being taken: ")
                app_date = input("Please input the date of the order using the YYYY-MM-DD format: ")
                user_input = (customer_id, app_tc_id, cert_id, app_date, app_id)
                #executes the sql query using the users inputs
                cursor.execute(app_sql_update, user_input)
                #commit statment to update the db as soon as the user finishes updating the data
                cursor.connection.commit()
                print("Appointment updated successfully")
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")
        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")
    #option 3 logic
    if action_choice == '3':
        prompt = input("You have selected to delete a record. Would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
            #list of the tables available to delete a record from
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
            table_selection = input("Please enter the number of the table containing the record you want to delete: ")
            #if the user decides to delete a record from the customer_info table
            if table_selection == "1":
                #sql delete query for customer_info table
                cust_info_sql_delete = "DELETE FROM CUSTOMER_INFO WHERE CUSTOMER_ID = ?"
                chosen_customer = input("Please input the customer ID number of the customer you want to delete: ")
                #executes the sql statement using the users input
                cursor.execute(cust_info_sql_delete, (chosen_customer,))
                #commit statement to update the db after the customer has been deleted
                cursor.connection.commit()
                print("Customer deleted successfully")
            #if the user decides to delete a record from the testing center_info table
            if table_selection == "2":
                #sql delete query for testing_center_info table
                #test_cent_sql_delete = "DELETE FROM TESTING_CENTER_INFO WHERE TC_ID = ?"
                #chosen_testing_center= input("Please input the testing center ID number of the ceneter you want to delete:")
                #executes the sql statement using the users input
                #cursor.execute(test_cent_sql_delete, (chosen_testing_center,))
                #commit statement to update the db after the customer has been deleted
                #cursor.connection.commit()
                #print("Testing center deleted successfully")
                pass
            #if the user decides to delete a record from the cert_orders table
            if table_selection == "3":
                #sql delete query for cert_orders table
                cert_order_sql_delete = "DELETE FROM CERT_ORDERS WHERE ORDER_ID = ?"
                chosen_order= input("Please input the order ID number of the order you want to delete:")
                #executes the sql statement using the users input
                cursor.execute(cert_order_sql_delete, (chosen_order,))
                #commit statement to update the db after the customer has been deleted
                cursor.connection.commit()
                print("Order deleted successfully")
            if table_selection == "4":
                pass
            if table_selection == "5":
                pass
            if table_selection == "6":
                pass
            #if the user decides to delete from the appointment table
            if table_selection == "7":
                #sql delete query for appointment table
                app_sql_delete = "DELETE FROM APPOINTMENTS WHERE APP_ID = ?"
                chosen_app= input("Please input the ID number of the appointment you want to delete: ")
                #executes the sql statement using the users input
                cursor.execute(app_sql_delete, (chosen_app,))
                #commit statement to update the db after the appointment has been deleted
                cursor.connection.commit()
                print("Appointment deleted successfully")
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

    #option 4 logic
    if action_choice == '4':
        prompt = input("You have selected to search for a record. Would you like to continue (Y/N)? ").upper()
        if prompt == "Y":
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
            table_selection = input("Please enter the number of the table containing the record you want to search for:")
            #if the user searches for a record in the customer_info table
            if table_selection == "1":
                cust_search_query = "SELECT * FROM CUSTOMER_INFO WHERE CUSTOMER_ID = ?"
                cust_ID = input("Please input the customer ID of the customer you need information for: ")
                cursor.execute(cust_search_query, (cust_ID,))
                record = cursor.fetchall()
                for field in record:
                    print("Customer ID = ", field[0] )
                    print("Customer Name = ", field[1])
                    print("Customer Address = ", field[2])
                    print("Customer City  = ", field[3])
                    print("Customer State = ", field[4])
                    print("Customer Sign Up Date = ", field[5])
                    print("Customer Prefered Testing Center = ", field[6])
                    print("Customer Email = ", field[7], "\n")
            #if the user searches for a record in the testing_center_info table
            if table_selection == "2":
                TC_search_query = "SELECT * FROM TESTING_CENTER_INFO WHERE TC_ID = ?"
                user_tc_id = input("Please input the Testing Center ID of the center you need information for: ")
                cursor.execute(TC_search_query, (user_tc_id,))
                record = cursor.fetchall()
                for field in record:
                    print("Testing Center ID = ", field[0] )
                    print("Testing Center Name = ", field[1])
                    print("Testing Center Address = ", field[2])
                    print("Testing Center City  = ", field[3])
                    print("Testing Center State = ", field[4])
                    print("Testing Center Zip = ", field[5])
                    print("Testing Center Hours of Operation = ", field[6], "\n")
            #if the user searches for a record in the cert_orders table
            if table_selection == "3":
                order_search_query = "SELECT * FROM CERT_ORDERS WHERE ORDER_ID = ?"
                user_order_id = input("Please input the order ID of the order you need information for: ")
                cursor.execute(order_search_query, (user_order_id,))
                record = cursor.fetchall()
                for field in record:
                    print("Order ID = ", field[0] )
                    print("Ordering Customer ID = ", field[1])
                    print("Certification ID of Certification Ordered = ", field[2])
                    print("Order Date = ", field[3])
                    print("Order Cost = ", field[4], "\n")

            if table_selection == "4":
                pass
            if table_selection == "5":
                pass
            if table_selection == "6":
                pass
            #if the user wants to search the appointments table
            if table_selection == "7":
                app_search_query = "SELECT * FROM APPOINTMENTS WHERE APP_ID = ?"
                user_app_id = input("Please input the appointment ID of the appointment you need information for: ")
                cursor.execute(app_search_query, (user_app_id,))
                record = cursor.fetchall()
                for field in record:
                    print("Appointment ID = ", field[0] )
                    print("Customer ID of the customer who made the appointment = ", field[1])
                    print("Testing Center ID where appointment is scheduled = ", field[2])
                    print("Certification ID of the exam being taken = ", field[3])
                    print("Appointment Date = ", field[4], "\n")
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

    #option 5 logic
    if action_choice == '5':
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

                #currently just shows all the appointments needs to be adjusted so it shows better data
                #possibly upcoming appointments for each testing center.
                if report_choice == '3':
                    count_appointments = "SELECT COUNT(APP_ID) AS NUM_OF_APP FROM APPOINTMENTS "
                    data =cursor.execute(count_appointments).fetchall()
                    actual_count = data[0]

                    print("\nThere are "+str(actual_count[0]) +" upcoming appointments.")

                    leave_report = 'Y'
                    menu_print()
                    action_choice = input("\nReturning to main menu\nPlease type the number infront of the action you would like to take: ")

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
                    prompt = input("You have selected to exit the report menu. Would you like to continue (Y/N)? \n").upper()
                    if prompt == 'Y':
                        leave_report = prompt
                        menu_print()
                        action_choice = input("Please type the number infront of the action you would like to take: ")
                    else:
                        report_choice = input("Please select a report to generate: ")
        
        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

        

    #option 6 logic
    if action_choice == '6':
        prompt = input("You have selected to exit the program. Would you like to continue (Y/N)? \n").upper()
        if prompt == "Y":
            leave = prompt
            print("\n| {:^24} |".format('Exiting the C^2 Database Menu'))
        else:
            menu_print
            action_choice = input("Please type the number infront of the action you would like to take: ")
    #This code below introduces a bug 
    #else:
        #print ("Selection invalid. Please enter an appropriate selection...")
        #menu_print()
        #action_choice = input("Please choose an option on the list: ")
        



#commits statements and closes connection
cursor.connection.commit()
cursor.close()
