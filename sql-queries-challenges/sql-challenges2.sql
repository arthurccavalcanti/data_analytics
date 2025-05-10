-- Assessment Test 3
/*
Create a new database called "School". This database should have two tables: teachers and students.
The students table should have columns for student_id, first_name,last_name, homeroom_number, phone,email, and graduation year.
The teachers table should have columns for teacher_id, first_name, last_name, homeroom_number, department, email, and phone.
The constraints are mostly up to you, but your table constraints do have to consider the following:
    1.  We must have a phone number to contact students in case of an emergency.
    2.  We must have ids as the primary key of the tables
    3. Phone numbers and emails must be unique to the individual.
Once you've made the tables, insert a student named Mark Watney (student_id=1) who has a phone number of 777-555-1234 and doesn't have an email. He graduates in 2035 and has 5 as a homeroom number.
Then insert a teacher named Jonas Salk (teacher_id = 1) who has a homeroom number of 5 and is from the Biology department. His contact info is: jsalk@school.org and a phone number of 777-555-4321.
*/

	CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	homeroom_number SMALLINT CHECK(homeroom_number > 0),
	phone TEXT NOT NULL UNIQUE,
	email TEXT UNIQUE,
	graduation_year SMALLINT CHECK(graduation_year > 1900),
	CHECK(first_name != last_name)
);

	CREATE TABLE teachers(
	teacher_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	homeroom_number SMALLINT CHECK(homeroom_number > 0),
	phone TEXT NOT NULL UNIQUE,
	email TEXT UNIQUE,
	department TEXT NOT NULL,
	CHECK(first_name != last_name)
)

INSERT INTO students(first_name, last_name, phone, email, graduation_year, homeroom_number)
VALUES('Mark','Watney','777-555-1234',null,2035,5);

INSERT INTO teachers(first_name, last_name, phone, email, department, homeroom_number)
VALUES('Jonas','Salk','777-555-4321','jsalk@school.org','Biology',5);



--  1. We want to know and compare the various amounts of films we have per movie rating. Use CASE and the dvdrental database to re-create this table:

SELECT DISTINCT rating FROM film;

-- This returns PG, R, G, PG-13, NC-17.

SELECT SUM(
CASE rating
	WHEN 'PG' THEN 1
	ELSE 0
END) AS PG,
SUM(CASE rating
	WHEN 'R' THEN 1
	ELSE 0
END) AS R,
SUM(CASE rating
	WHEN 'G' THEN 1
	ELSE 0
END) AS G,
SUM(CASE rating
	WHEN 'PG-13' THEN 1
	ELSE 0
END) AS PG13,
SUM(CASE rating
	WHEN 'NC-17' THEN 1
	ELSE 0
END) AS NC17
FROM film;