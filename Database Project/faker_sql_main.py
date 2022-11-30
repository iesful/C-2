# note: you MUST have installed the faker module and sqlite3 
# through pip for these imports to work on your own machine 
import faker, sqlite3, os, datetime, random
from prettytable import PrettyTable
import faker.providers.address.en_US

#inserts new records into customer info table
def insert_into_customer_info(name, street, city, state, signup_date, tc_id, email):
    cursor.execute("\
        INSERT INTO CUSTOMER_INFO (NAME, STREET, CITY, STATE, SIGNUP_DATE, TC_ID, EMAIL)\
        VALUES (?, ?, ?, ?, ?, ?, ?)", (name, street, city, state, signup_date, tc_id, email))

    print("Record inserted into Customer_Info...")

#inserts new records into testing center info table
def insert_into_testing_center_info(name, street, city, state, postal):
    cursor.execute("\
        INSERT INTO TESTING_CENTER_INFO (TC_NAME, STREET, CITY, STATE, ZIP, HOURS)\
        VALUES (?, ?, ?, ?, ?, 'M - F, 9AM - 5PM')", (name, street, city, state, postal))

    print("Record inserted into Testing_Center_Info...")

#inserts new records into test taker info table
def insert_into_test_taker_info(customer_id, cert_id, tc_id, actual_score, time_used, date_taken):
    cursor.execute("\
        INSERT INTO TEST_TAKER_INFO (CUSTOMER_ID, CERT_ID, TC_ID, ACTUAL_SCORE, TIME_USED, DATE_TAKEN)\
            VALUES (?, ?, ?, ?, ?, ?)", (customer_id, cert_id, tc_id, actual_score, time_used, date_taken))

    print("Record inserted Test_Taker_Info...")

#inserts records into appointments table
def insert_into_appointments(customer_id, tc_id, cert_id, app_date):
    cursor.execute("\
        INSERT INTO APPOINTMENTS (CUSTOMER_ID, TC_ID, CERT_ID, APP_DATE)\
            VALUES (?, ?, ?, ?)", (customer_id, tc_id, cert_id, app_date))

    print("Record inserted into Appointments...")
    
#inserts into cert_orders table
def insert_into_cert_orders(customer_id, cert_id, order_date, order_cost):
    cursor.execute("\
        INSERT INTO CERT_ORDERS (CUSTOMER_ID, CERT_ID, ORDER_DATE, ORDER_COST)\
            VALUES (?, ?, ?, ?)", (customer_id, cert_id, order_date, order_cost))

    print("Record inserted into Cert_Orders...")

#prints options menu
def menu_print():
    menu = "\n\
        {:^24}  \n\n\
    |0. {:^24} |\n\
    |1. {:^24} |\n\
    |2. {:^24} |\n\
    |3. {:^24} |\n\
    |4. {:^24} |\n\
    |5. {:^24} |\n\
    |6. {:^24} |\n"

    print(menu.format('C^2 Database Menu','View records', 'Add a new record', 'Modify a record',
    'Delete a record', 'Search for a record', 'View reports', 'Quit'))

#faker obj, db name, and db validation
fake = faker.Faker('en_US')
db_name = "C^2.db"
validate_db = os.path.exists(db_name)

#validates the existance of the db and creates it if nonexistant
if validate_db:
    print(f"Database with name: {db_name} found, fetching data and connecting... \n")
    con = sqlite3.connect(db_name)
    cursor = con.cursor()    
else:
    print(f"No database found with name: {db_name}, generating new DB...")
    con = sqlite3.connect(db_name)
    cursor = con.cursor()

    #creates customer info table
    cursor.execute("\
        CREATE TABLE CUSTOMER_INFO ( \
            CUSTOMER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            NAME VARCHAR(255) NOT NULL, \
            STREET VARCHAR(50) NOT NULL, \
            CITY VARCHAR(30) NOT NULL, \
            STATE VARCHAR(2) NOT NULL, \
            SIGNUP_DATE DATE NOT NULL, \
            TC_ID INT NOT NULL,\
            EMAIL VARCHAR(100) NOT NULL,\
            FOREIGN KEY (TC_ID) REFERENCES TESTING_CENTER_INFO(TC_ID) \
        );")

    print("CUSTOMER_INFO TABLE CREATED...")
    
    #creates test taker info table
    cursor.execute("\
        CREATE TABLE TEST_TAKER_INFO (\
            EXAM_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            CUSTOMER_ID INT NOT NULL, \
            CERT_ID INT NOT NULL,\
            TC_ID INT NOT NULL,\
            ACTUAL_SCORE INT NOT NULL,\
            TIME_USED VARCHAR(20) NOT NULL,\
            DATE_TAKEN SMALLDATE NOT NULL, \
            FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER_INFO(CUSTOMER_ID),\
            FOREIGN KEY (TC_ID) REFERENCES TESTING_CENTER_INFO(TC_ID),\
            FOREIGN KEY (CERT_ID) REFERENCES CERTIFICATION_INFO(CERT_ID)\
        );")
    print("TEST_TAKER_INFO TABLE CREATED...")

    #creates testing center info table
    cursor.execute("\
        CREATE TABLE TESTING_CENTER_INFO (\
            TC_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
            TC_NAME VARCHAR(40) NOT NULL,\
            STREET VARCHAR(50) NOT NULL,\
            CITY VARCHAR(25) NOT NULL,\
            STATE VARCHAR(2) NOT NULL,\
            ZIP VARCHAR(5) NOT NULL,\
            HOURS VARCHAR(50) NOT NULL\
        );")
    print("TESTING_CENTER_INFO TABLE CREATED...")

    #creates cert orders table
    cursor.execute("\
        CREATE TABLE CERT_ORDERS (\
            ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
            CUSTOMER_ID INT NOT NULL,\
            CERT_ID INT NOT NULL,\
            ORDER_DATE SMALLDATE NOT NULL,\
            ORDER_COST FLOAT(5,2) NOT NULL,\
            FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER_INFO(CUSTOMER_ID),\
            FOREIGN KEY (CERT_ID) REFERENCES CERTIFICATION_INFO(CERT_ID)\
        );")
    print("CERT_ORDERS TABLE CREATED...")

    #creates certification info table
    cursor.execute("\
        CREATE TABLE CERTIFICATION_INFO (\
            CERT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
            CERT_NAME VARCHAR(50) NOT NULL,\
            EXAM_CODE VARCHAR(10) NOT NULL,\
            PRICE INT NOT NULL,\
            TEST_DURATION INT NOT NULL,\
            PASSING_SCORE INT NOT NULL,\
            RENEWABLE BOOLEAN NOT NULL,\
            NUM_OF_QUESTIONS INT NOT NULL\
        );")
    print("CERTIFICATION_INFO TABLE CREATED...")

    #creats job infor table
    cursor.execute("\
        CREATE TABLE JOB_INFO_OPPORTUNITIES (\
            JOB_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
            JOB_TITLE VARCHAR(100) NOT NULL,\
            SALARY VARCHAR(10) NOT NULL,\
            CERT_ID INT NOT NULL,\
            FOREIGN KEY (CERT_ID) REFERENCES CERTIFICATION_INFO(CERT_ID)\
        );")
    print("JOB_INFO_OPPORTUNITIES TABLE CREATED...")

    #creates appointments table
    cursor.execute("\
        CREATE TABLE APPOINTMENTS (\
            APP_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
            CUSTOMER_ID INT NOT NULL,\
            TC_ID INT NOT NULL,\
            CERT_ID INT NOT NULL,\
            APP_DATE DATE NOT NULL,\
            FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER_INFO(CUSTOMER_ID),\
            FOREIGN KEY (TC_ID) REFERENCES TESTING_CENTER_INFO(TC_ID),\
            FOREIGN KEY (CERT_ID) REFERENCES CERTIFICATION_INFO(CERT_ID)\
        );")
    print("APPOINTMENTS TABLE CREATED...")

    #inserts records into certification_info table
    cursor.execute('\
        INSERT INTO CERTIFICATION_INFO (CERT_NAME, EXAM_CODE, PRICE, TEST_DURATION, PASSING_SCORE, RENEWABLE, NUM_OF_QUESTIONS)\
            VALUES ("IT Fundamentals (ITF+)", "FC0-U61", 134.00, 60, 650, FALSE, 75),\
            ("A+", "220-1001", 246.00, 90, 675, TRUE, 90),\
            ("A+", "220-1002", 246.00, 90, 700, TRUE, 90),\
            ("A+", "220-1101", 246.00, 90, 675, TRUE, 90),\
            ("A+", "220-1102", 246.00, 90, 700, TRUE, 90),\
            ("Network+", "N10-007", 358.00, 90, 720, TRUE, 90),\
            ("Network+", "N10-008", 358.00, 90, 720, TRUE, 90),\
            ("Security+", "SY0-601", 392.00, 90, 750, TRUE, 90),\
            ("Cloud+", "CV0-002", 358.00, 90, 750, TRUE, 90),\
            ("Cloud+", "CV0-003", 358.00, 90, 750, TRUE, 90),\
            ("Linux+", "XK0-004", 358.00, 90, 720, TRUE, 90),\
            ("Linux+", "XK0-005", 358.00, 90, 720, TRUE, 90),\
            ("Server+", "SK0-004", 358.00, 90, 750, FALSE, 100),\
            ("Server+", "SK0-005", 358.00, 90, 750, FALSE, 90),\
            ("Cyber Security Analyst (CySA)", "CS0-002", 392.00, 165, 750, FALSE, 85),\
            ("Pentest+","PT0-001", 392.00, 165, 750, TRUE, 85),\
            ("Pentest+","PT0-002", 392.00, 165, 750, TRUE, 85),\
            ("CompTIA Advanced Security Practitioner (CASP+)", "CAS-003", 494.00, 165, 100, TRUE, 90),\
            ("CompTIA Advanced Security Practitioner (CASP+)", "CAS-004", 494.00, 165, 100, TRUE, 90),\
            ("Data+", "DA0-001", 246.00, 90, 675, TRUE, 90),\
            ("Certified Technical Trainer (CTT+)", "TK0-201", 358.00, 90, 655, FALSE, 95),\
            ("Cloud Essentials+", "CLO-002", 134.00, 60, 720, FALSE, 75),\
            ("Project+", "PK0-004", 358.00, 90, 710, FALSE, 95),\
            ("Project+", "PK0-005", 358.00, 90, 710, FALSE, 90)\
            ;')
    print("CERTIFICATION_INFO records created...")

    #fetches all cert ids
    certs = cursor.execute("SELECT * FROM CERTIFICATION_INFO").fetchall()
    job_statement = "\
        INSERT INTO JOB_INFO_OPPORTUNITIES (JOB_TITLE, SALARY, CERT_ID)\
            VALUES ('Help Desk Technician', 43931, IT Fundamentals (ITF+)),\
            ('Desktop Support Specialist', 53835, A+),\
            ('Network Engineer', 77040, Network+),\
            ('Systems Administrator', 64157, Security+),\
            ('Cloud Engineer', 92504, Cloud+),\
            ('Linux System Administrator', 79961, Linux+),\
            ('Data Center Technician', 58260, Server+),\
            ('Security Analyst', 70562, Cyber Security Analyst (CySA)),\
            ('Penetration Tester', 88545, Pentest+),\
            ('Security Architect', 130989, CompTIA Advanced Security Practitioner (CASP+)),\
            ('Data Analyst', 63577, Data+),\
            ('Training Consultant', 58613, Certified Technical Trainer (CTT+)),\
            ('Business Analyst', 71358, Cloud Essentials+),\
            ('IT Project Manager', 89355, Project+);"

    #loops through cert ids and replaces cert names with id
    for i in range(len(certs)):
        if certs[i][1] in job_statement:
            job_statement = job_statement.replace(certs[i][1], str(certs[i][0]))

    #executes insert statement
    cursor.execute(job_statement)
    print("JOB_INFO_OPPORTUNITIES records created...")

    #loop to insert records into customer info table
    for _ in range(15):
        insert_into_customer_info(fake.name(), fake.street_address(), fake.city(), 'TX', datetime.date.today(), random.randint(1,15), fake.ascii_free_email())
        
    #loop to insert records into testing center info table
    for _ in range(15):
        insert_into_testing_center_info(fake.company(), fake.street_address(), fake.city(), 'TX', fake.postalcode_in_state('TX'))

    #functionality to generate random orders
    customer = cursor.execute("SELECT * FROM CUSTOMER_INFO").fetchall()
    certification = cursor.execute("SELECT * FROM CERTIFICATION_INFO").fetchall()
    for _ in range(15):
        ids = customer[random.randint(0,len(customer)-1)][0]
        cert = certification[random.randint(0,len(certification)-1)]
        cert_ids = cert[0]
        cost = cert[3]

        insert_into_cert_orders(ids, cert_ids, datetime.date.today(), cost)

    #new functionality to generate random test taker records
    data = cursor.execute("SELECT * FROM CERT_ORDERS").fetchall()
    customer_data = cursor.execute("SELECT * FROM CUSTOMER_INFO").fetchall()
    for i in range(15):
        customer_ids = data[i][1]
        certification_id = data[i][2]

        y = 0
        while True:
            if customer_data[y][0] == customer_ids:
                testingcenter = customer_data[y][6]
                break
            else:
                y += 1

        if certification_id in [18, 19]:
            actual_score = random.randint(0,100)
        else:
            actual_score = random.randint(400, 900)

        if certification_id in [15, 16, 17, 18, 19]:
            time_used = random.randint(20, 165)
        else:
            time_used = random.randint(20,90)

        date_taken = datetime.date.today() + datetime.timedelta(days=7.0)

        insert_into_test_taker_info(customer_ids, certification_id, testingcenter, actual_score, time_used, date_taken)

    #functionality to generate appointments
    orders_data = cursor.execute("SELECT * FROM CERT_ORDERS").fetchall()
    customer_data = cursor.execute("SELECT * FROM CUSTOMER_INFO").fetchall()
    for i in range(15):
        customerid = orders_data[i][1]
        certificationid = orders_data[i][2]

        y = 0
        while True:
            if customer_data[y][0] == customerid:
                testingcenter = customer_data[y][6]
                break
            else:
                y += 1

        app_date = datetime.date.today() + datetime.timedelta(days=7.0)

        insert_into_appointments(customerid, testingcenter, certificationid, app_date)

#options menu
menu_print()

#takes the user's choice from the menu options
action_choice = input("Please type the number infront of the action you would like to take: ")

leave = 'N'
while leave != "Y":
    #if the user decides to view all records of a table
    if action_choice == "0":
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
                myTable = PrettyTable(["CUSTOMER_ID", "NAME", "STREET", "CITY", "STATE", "SIGNUP_DATE", "TC_ID", "EMAIL"])
                myresult = cursor.fetchall()
                for x in myresult:
                    myTable.add_row(x)
                print(myTable)
                menu_print()
                action_choice = int(input("Please type the number infront of the action you would like to take: "))
                
            if table_selection == "2":
                print("Displaying TESTING_CENTER_INFO Table Records:")
                print()
                cursor.execute("SELECT * FROM TESTING_CENTER_INFO")
                myTable = PrettyTable(['TC_ID', 'TC_NAME', 'STREET', 'CITY', 'STATE', 'ZIP', 'HOURS'])
                myresult = cursor.fetchall()
                for x in myresult:
                    myTable.add_row(x)
                print(myTable)
                menu_print()
                action_choice = int(input("Please type the number infront of the action you would like to take: "))
            
            if table_selection == "3":
                print("Displaying CERT_ORDERS Table Records:")
                print()
                cursor.execute("SELECT * FROM CERT_ORDERS")
                myTable = PrettyTable(['ORDER_ID', 'CUSTOMER_ID', 'CERT_ID', 'ORDER_DATE', 'ORDER_COST'])
                myresult = cursor.fetchall()
                for x in myresult:
                    myTable.add_row(x)
                print(myTable)
                menu_print()
                action_choice = int(input("Please type the number infront of the action you would like to take: "))
            
            if table_selection == "4":
                print("Displaying TEST_TAKER_INFO Table Records:")
                print()
                cursor.execute("SELECT * FROM TEST_TAKER_INFO")
                myTable = PrettyTable(['EXAM_ID', 'CUSTOMER_ID', 'CERT_ID', 'TC_ID', 'ACTUAL_SCORE', 'TIME_USED', 'DATE_TAKEN'])
                myresult = cursor.fetchall()
                for x in myresult:
                    myTable.add_row(x)
                print(myTable)
                menu_print()
                action_choice = int(input("Please type the number infront of the action you would like to take: "))
                
            if table_selection == "5":
                print("Displaying CERTIFICATION_INFO Table Records:")
                print()
                cursor.execute("SELECT * FROM CERTIFICATION_INFO")
                myresult = cursor.fetchall()
                myTable = PrettyTable(['CERT_ID', 'CERT_NAME', 'EXAM_CODE', 'PRICE', 'TEST_DURATION', 'PASSING_SCORE', 'RENEWABLE', 'NUM_OF_QUESTIONS'])
                for x in myresult:
                    myTable.add_row(x)
                print(myTable)
                menu_print()
                action_choice = int(input("Please type the number infront of the action you would like to take: "))
                
            if table_selection == "6":
                print("Displaying JOB_INFO_OPPORTUNITIES Table Records:")
                print()
                cursor.execute("SELECT * FROM JOB_INFO_OPPORTUNITIES")
                myresult = cursor.fetchall()
                myTable = PrettyTable(["JOB_ID", "JOB_TITLE", "SALARY", "CERT_ID"])
                for x in myresult:
                    myTable.add_row(x)
                print(myTable)
                menu_print()
                action_choice = int(input("Please type the number infront of the action you would like to take: "))
            
            if table_selection == "7":
                print("Displaying APPOINTMENTS Table Records:")
                print()
                cursor.execute("SELECT * FROM APPOINTMENTS")
                myTable = PrettyTable(['APP_ID', 'CUSTOMER_ID', 'TC_ID', 'CERT_ID', 'APP_DATE'])
                myresult = cursor.fetchall()
                for x in myresult:
                    myTable.add_row(x)
                print(myTable)
                menu_print()
                action_choice = int(input("Please type the number infront of the action you would like to take: "))
            
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")
        else:
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
    |3. {:^24} |\n"

            print(tables.format('Tables', 'CUSTOMER_INFO','CERT_ORDERS','APPOINTMENTS'))

            table_selection = input("Please enter the number of the table you would like to add a record to: ")

            #if the user decides to add to customer_info table
            if table_selection == "1":

                #all the fields that need to be populated to create a record in the customer_info table
                entered_name = input("Please input the name of the customer (e.g: Firstname Lastname): ")
                entered_street = input("Please enter the customer's street address (e.g: 1234 Main Street): ")
                entered_city = input("Please input the customer's city (e.g: Houston): ")
                entered_state = input("Please input the customer's state abbreviation (e.g: TX): ").upper()
                entered_date = datetime.date.today()
                entered_TC_ID = input("Please enter the customer's preferred Testing Center ID (Pick from 1-15): ")
                entered_email = input("Please input the customer's email address (e.g.: BobSmith@gmail.com): ")

                #use the same function created at the beginning to insert into the customer_info table 
                insert_into_customer_info(entered_name, entered_street, entered_city, entered_state, entered_date, entered_TC_ID, entered_email)
                
                #commit statemtent so the db is updated as soon as you finish entering the data
                cursor.connection.commit()
                print("Returning to main menu...")

            #if the user decides to add to the cert_orders table
            if table_selection == "2":
                #all the fields that need to be populated to creat a record in the cert_orders table
                entered_cust_ID = input("Please enter the customer ID of the customer making the order: ")
                entered_cert_ID = input("Please enter the cert ID for the certification being ordered: ")
                entered_order_date = datetime.date.today()
                entered_order_cost = input("Please enter the cost of the cert being ordered:")
                #use the function to inser tinto the cert_orders table
                insert_into_cert_orders(entered_cust_ID, entered_cert_ID, entered_order_date, entered_order_cost)
                #commit statement so the db is updated as soon as you finish entering the data
                cursor.connection.commit()
                print("Returning to main menu...")

            #if the user decides to add to the appointments table
            if table_selection == "3":
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
    |4. {:^24} |\n"

            print(tables.format('Tables', 'CUSTOMER_INFO','TESTING_CENTER_INFO',
             'CERT_ORDERS','APPOINTMENTS' ))
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
                order_id = input("Please input the ID number of the order you want to update:")
                customer_id = input("Please input the ID number of the customer who made the order:")
                cert_id = input("Please input the ID number of the cert being ordered:")
                order_date = input("Please input the date of the order using the YYYY-MM-DD format:")
                order_cost = input("Please input the ordercost according to the cert ordered:")
                user_input = (customer_id, cert_id, order_date, order_cost, order_id)
                #executes the sql query using the users inputs
                cursor.execute(cert_orders_sql_update, user_input)
                #commit statment to update the db as soon as the user finishes updating the data
                cursor.connection.commit()
                print("Order updated successfully")

            if table_selection == "4":
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
                app_date = input("Please input the date of the appointment using the YYYY-MM-DD format: ")
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
    |3. {:^24} |\n"

            print(tables.format('Tables', 'CUSTOMER_INFO','CERT_ORDERS','APPOINTMENTS' ))
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
            
            #if the user decides to delete a record from the cert_orders table
            if table_selection == "2":
                #sql delete query for cert_orders table
                cert_order_sql_delete = "DELETE FROM CERT_ORDERS WHERE ORDER_ID = ?"
                chosen_order= input("Please input the order ID number of the order you want to delete:")
                #executes the sql statement using the users input
                cursor.execute(cert_order_sql_delete, (chosen_order,))
                #commit statement to update the db after the customer has been deleted
                cursor.connection.commit()
                print("Order deleted successfully")

            #if the user decides to delete from the appointment table
            if table_selection == "3":
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
    |4. {:^24} |\n"

            print(tables.format('Tables', 'CUSTOMER_INFO','TESTING_CENTER_INFO','CERT_ORDERS','APPOINTMENTS' ))
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

            #if the user wants to search the appointments table
            if table_selection == "4":
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
                    print()
                    cursor.execute('''
                    SELECT 
                    TEST_TAKER_INFO.CUSTOMER_ID,
                    COUNT(TEST_TAKER_INFO.CERT_ID) AS value_occurrence,
                    TEST_TAKER_INFO.CERT_ID,
                    CERTIFICATION_INFO.CERT_NAME
                    FROM TEST_TAKER_INFO
                    LEFT JOIN CERTIFICATION_INFO ON TEST_TAKER_INFO.CERT_ID = CERTIFICATION_INFO.CERT_ID
                    ORDER BY value_occurrence DESC
                    LIMIT 1;
                     ''')
                    output = cursor.fetchall()
                    print()
                    for items in output:
                        print(f"{items[3]} Is the most popular certification among test takers. Its Certification ID is: {items[3]}.\n This could indicate that this is an In-demand Certification worth obtaining.")
                    print()
                    leave_report = 'Y'
                    menu_print()
                    action_choice = input("\nReturning to main menu\nPlease type the number infront of the action you would like to take: ")
                    

                if report_choice == '5':
                    print()
                    cursor.execute('''
                    SELECT 
                    TEST_TAKER_INFO.DATE_TAKEN,
                    TEST_TAKER_INFO.ACTUAL_SCORE,  
                    TEST_TAKER_INFO.CUSTOMER_ID, 
                    CERTIFICATION_INFO.CERT_ID, 
                    CERTIFICATION_INFO.CERT_NAME, 
                    CUSTOMER_INFO.NAME 
                    FROM TEST_TAKER_INFO
                    LEFT JOIN CUSTOMER_INFO ON TEST_TAKER_INFO.CUSTOMER_ID = CUSTOMER_INFO.CUSTOMER_ID,
                    LEFT JOIN CERTIFICATION_INFO ON TEST_TAKER_INFO.CERT_ID = CERTIFICATION_INFO.CERT_ID
                    WHERE TEST_TAKER_INFO.ACTUAL_SCORE = (SELECT MAX(TEST_TAKER_INFO.ACTUAL_SCORE) FROM TEST_TAKER_INFO);
                    ''')
                    
                    output = cursor.fetchall()
                    print()
                    for items in output:
                        print(f"{items[-1]} managed to achieve the highest score of all examinees with a whooping {items[-5]} out of 900 possible points!\nThey achieved this on the {items[-2]} Exam on {items[-6]}. Congratualations {items[-1]}. \n This may gives us insight as to which CompTIA exam may be easier to pass amongst others.")
                    print()
                    leave_report = 'Y'
                    menu_print()
                    action_choice = input("\nReturning to main menu\nPlease type the number infront of the action you would like to take: ")

                if report_choice == '6':
                    cursor.execute('''
                    SELECT 
                    COUNT(TEST_TAKER_INFO.TC_ID) AS value_occurrence,
                    TEST_TAKER_INFO.TC_ID,
                    TESTING_CENTER_INFO.TC_NAME
                    FROM TEST_TAKER_INFO 
                    LEFT JOIN TESTING_CENTER_INFO ON TEST_TAKER_INFO.TC_ID = TESTING_CENTER_INFO.TC_ID
                    ORDER BY value_occurrence ASC
                    LIMIT 1;
                     ''')
                    output = cursor.fetchall()
                    print()
                    for items in output:
                        print(f"The most favorated Testing Center among examinees is The {items[2]} Testing Center.\n Its Testing Center ID is: {items[1]}.\nThis may indicate that this Testing Center is well liked amongst examinees.")
                    print()
                    leave_report = 'Y'
                    menu_print()
                    action_choice = input("\nReturning to main menu\nPlease type the number infront of the action you would like to take: ")

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
                    print(report_menu.format('Report Menu', 'Most Expensive Certifications', 'Quickest Examinee', 'Number of Upcoming Appointments',
                    'List of all Certifications', 'Highest Scoring Examinee', 'Favorite Testing Center', 'Top 3 Most Expensive Orders',
                    'Most Positive Testing Date', 'List of all Jobs', 'Highest Paying Job', 'Return to Main Menu'))
                    report_choice = input("Selection invalid. Please chose an option from the list:")

        
        else:
            menu_print()
            action_choice = input("Please type the number infront of the action you would like to take: ")

        

    #option 6 logic
    if action_choice == '6':
        prompt = input("You have selected to exit the program. Would you like to continue (Y/N)?").upper()
        if prompt == "Y":
            leave = prompt
            print("\n| {:^24} |".format('Exiting the C^2 Database Menu'))
        else:
            menu_print
            action_choice = input("Please type the number infront of the action you would like to take: ")
    #for an valid choice
    if not action_choice == "0" or action_choice == "1" or action_choice == "2" or action_choice == "3" or action_choice == "4" or action_choice == "5" or action_choice == "6":
        menu_print()
        action_choice = input("Selection invalid. Please choose an option on the list: ")
        



#commits statements and closes connection to the database
cursor.connection.commit()
cursor.close()