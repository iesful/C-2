# note: you MUST have installed the faker module and sqlite3 
# through pip for these imports to work on your own machine
import faker, sqlite3, os, datetime, random
import faker.providers.address.en_US

#inserts new records into customer info table
def insert_into_customer_info(name, street, city, state, signup_date, tc_id, email):
    cursor.execute("\
        INSERT INTO CUSTOMER_INFO (NAME, STREET, CITY, STATE, SIGNUP_DATE, TC_ID, EMAIL)\
        VALUES (?, ?, ?, ?, ?, ?, ?)", (name, street, city, state, signup_date, tc_id, email))

    print("Record inserted...")

#inserts new records into testing center info table
def insert_into_testing_center_info(name, street, city, state, postal):
    cursor.execute("\
        INSERT INTO TESTING_CENTER_INFO (TC_NAME, STREET, CITY, STATE, ZIP, HOURS)\
        VALUES (?, ?, ?, ?, ?, 'M - F, 9AM - 5PM')", (name, street, city, state, postal))

    print("Record inserted...")

#inserts new records into test taker info table
def insert_into_test_taker_info(customer_id, cert_id, tc_id, actual_score, time_used, date_taken):
    cursor.execute("\
        INSERT INTO TEST_TAKER_INFO (CUSTOMER_ID, CERT_ID, TC_ID, ACTUAL_SCORE, TIME_USED, DATE_TAKEN)\
            VALUES (?, ?, ?, ?, ?, ?)", (customer_id, cert_id, tc_id, actual_score, time_used, date_taken))

    print("Inserting into Test_Taker_Info...")

#inserts records into appointments table
def insert_into_appointments(customer_id, tc_id, cert_id, app_date):
    cursor.execute("\
        INSERT INTO APPOINTMENTS (CUSTOMER_ID, TC_ID, CERT_ID, APP_DATE)\
            VALUES (?, ?, ?, ?)", (customer_id, tc_id, cert_id, app_date))

    print("Record inserted...")
    
#inserts into cert_orders table
def insert_into_cert_orders(customer_id, cert_id, order_date, order_cost):
    cursor.execute("\
        INSERT INTO CERT_ORDERS (CUSTOMER_ID, CERT_ID, ORDER_DATE, ORDER_COST)\
            VALUES (?, ?, ?, ?)", (customer_id, cert_id, order_date, order_cost))

    print("Inserting into CERT_ORDERS...")


#faker obj, db name, and db validation
fake = faker.Faker('en_US')
db_name = "C^2.db"
validate_db = os.path.exists(db_name)

#validates the existance of the db and creates it if nonexistant
if validate_db:
    print(f"Database with name: {db_name} found, fetching data and connecting...")
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
            CERT_ID INT NOT NULL\
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
    print("CERTIFICATION_INFO records inserted...")

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
    print("Records inserted into JOB_INFO_OPPORTUNITIES...")

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

    #functionality to generate appointments(FIX THIS)
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

#functionality to generate random test taker records
""" customer_ids = cursor.execute("SELECT CUSTOMER_ID FROM CUSTOMER_INFO").fetchall()
certification_id = cursor.execute("SELECT * FROM CERTIFICATION_INFO").fetchall()
testingcenter_id = cursor.execute("SELECT TC_ID FROM TESTING_CENTER_INFO").fetchall()
max_time = cursor.execute("SELECT TEST_DURATION FROM CERTIFICATION_INFO").fetchall()
for _ in range(15):
    cust_id = customer_ids[random.randint(0,len(customer_ids)-1)][0]
    cert = certification_id[random.randint(0,len(certification_id)-1)]
    cert_id = cert[0]
    tc_id = testingcenter_id[random.randint(0,len(testingcenter_id)-1)][0]
    actual_score = random.randint(500, 900)
    time_used = random.randint(20, cert[4])
    date_taken = datetime.date.today()
    attempt_num = random.randint(1, 5)

    insert_into_test_taker_info(cust_id, cert_id, tc_id, actual_score, time_used, date_taken, attempt_num) """


#commits statements and closes connection
cursor.connection.commit()
cursor.close()

