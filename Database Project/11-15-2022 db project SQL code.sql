drop database if exists CERTIFICATIONSDB;
create database CERTIFICATIONSDB;
use CERTIFICATIONSDB;
CREATE TABLE `Customer_Info` (
  `Customer_ID` int,
  `Firstname` varchar (15),
  `Lastname` varchar (15),
  `Street` varchar (50),
  `City` varchar (30),
  `State` varchar (2),
  `Signup_date` date,
  `TC_ID` int,
  PRIMARY KEY (`Customer_ID`)
);

CREATE TABLE `Cert_Orders` (
  `Order_ID` int,
  `Customer_ID` int,
  `Cert_ID` int,
  `Order_date` date,
  `Order_cost` float (5,2),
  PRIMARY KEY (`Order_ID`),
  FOREIGN KEY (`Customer_ID`) REFERENCES `Customer_Info`(`Customer_ID`)
);

CREATE TABLE `Certification_Info` (
  `Cert_ID` int,
  `Cert_Name` varchar (20),
  `Price` float (3,2),
  `Test_duration` varchar (20),
  `Passing_score` int,
  `Renewable` varchar (15),
  `Num_of_Questions` int,
  PRIMARY KEY (`Cert_ID`)
);

CREATE TABLE `Job_Opportunities` (
  `Job_ID` int,
  `Cert_ID` int,
  PRIMARY KEY (`Job_ID`),
  FOREIGN KEY (`Cert_ID`) REFERENCES `Certification_Info`(`Cert_ID`)
);

CREATE TABLE `Testing_Centers_info` (
  `TC_ID` int,
  `TC_Name` varchar (40),
  `Street` varchar (50),
  `City` varchar (25),
  `State` varchar (2),
  `Zip` varchar(5),
  `Hours` varchar (50),
  PRIMARY KEY (`TC_ID`)
);

CREATE TABLE `Test_Taker_Info` (
  `Exam_ID` int,
  `Customer_ID` int,
  `Cert_ID` int,
  `TC_ID` int,
  `Actual_score` int,
  `Time_used` varchar (20),
  `Date_Taken` date,
  `Attempt_Num` int,
  PRIMARY KEY (`Exam_ID`),
  FOREIGN KEY (`Customer_ID`) REFERENCES `Customer_Info`(`Customer_ID`),
  FOREIGN KEY (`Cert_ID`) REFERENCES `Certification_Info`(`Cert_ID`),
  FOREIGN KEY (`TC_ID`) REFERENCES `Testing_Centers_info`(`TC_ID`)
);

CREATE TABLE `Job_Info` (
  `Job_title` varchar (20),
  `Job_ID` int,
  `Salary` varchar (10),
  PRIMARY KEY (`Job_title`)
);







