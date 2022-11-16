# note: you MUST have installed the faker module and sqlite3 
# through pip for these imports to work on your own machine
import faker
import faker.providers.address.en_US
import sqlite3, os, datetime

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
            ATTEMPT_NUM INT NOT NULL,\
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

    #creates job opportunities table
    cursor.execute("\
        CREATE TABLE JOB_OPPORTUNITIES (\
            JOB_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
            CERT_ID INT NOT NULL,\
            FOREIGN KEY (CERT_ID) REFERENCES CERTIFICATION_INFO(CERT_ID)\
        );")
    print("JOB_OPPORTUNITIES TABLE CREATED...")

    #creats job infor table
    cursor.execute("\
        CREATE TABLE JOB_INFO (\
            JOB_TITLE VARCHAR(50) PRIMARY KEY NOT NULL,\
            JOB_ID INT NOT NULL,\
            SALARY VARCHAR(10) NOT NULL,\
            FOREIGN KEY (JOB_ID) REFERENCES JOB_OPPORTUNITIES(JOB_ID)\
        );")
    print("JOB_INFO TABLE CREATED...")



#loop to insert records into customer info table
for _ in range(15):
    insert_into_customer_info(fake.name(), fake.street_address(), fake.city(), 'TX', datetime.date.today(), 100, fake.ascii_free_email())
    
#loop to insert records into testing center info table
for _ in range(15):
    insert_into_testing_center_info(fake.company(), fake.street_address(), fake.city(), 'TX', fake.postalcode_in_state('TX'))


#inserts records into certification_info table
cursor.execute('\
    INSERT INTO CERTIFICATION_INFO (CERT_NAME, EXAM_CODE, PRICE, TEST_DURATION, PASSING_SCORE, RENEWABLE, NUM_OF_QUESTIONS)\
        VALUES ("IT Fundatmentals(ITF+)", "FC0-U61", 134.00, 60, 650, FALSE, 75),\
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
        ("Cybersecurity Analyst (CySA+)", "CS0-002", 392.00, 165, 750, FALSE, 85),\
        ("Pentest+","PT0-001", 392.00, 165, 750, TRUE, 85),\
        ("Pentest+","PT0-002", 392.00, 165, 750, TRUE, 85),\
        ("CompTIA Advanced Security Practitioner (CASP+)", "CAS-003", 494.00, 165, 100, TRUE, 90),\
        ("CompTIA Advanced Security Practitioner (CASP+)", "CAS-004", 494.00, 165, 100, TRUE, 90),\
        ("Data+", "DA0-001", 246.00, 90, 675, TRUE, 90),\
        ("Certified Technical Trainer (CTT+)", "TK0-201", 358.00, 90, 655, FALSE, 95),\
        ("Certified Technical Trainer (CTT+)", "TK0-202", 382.00, 22, 36, FALSE, 0),\
        ("Certified Technical Trainer (CTT+)", "TK0-203", 382.00, 22, 36, FALSE, 0),\
        ("Cloud Essentials+", "CLO-002", 134.00, 60, 720, FALSE, 75),\
        ("Project+", "PK0-004", 358.00, 90, 710, FALSE, 95),\
        ("Project+", "PK0-005", 358.00, 90, 710, FALSE, 90)\
        ;')
print("CERTIFICATION_INFO records inserted...")


#commits statements and closes connection
cursor.connection.commit()
cursor.close()