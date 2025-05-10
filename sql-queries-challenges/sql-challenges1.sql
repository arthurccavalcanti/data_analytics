-- 1. Return the customer IDs of customers who have spent at least $110 with the staff member who has an ID of 2.
SELECT customer_id, staff_id, SUM(amount)
FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) >110;

-- What customer has the highest customer ID number whose name starts with an 'E' and has an address ID lower than 500?
SELECT first_name, last_name FROM customer
WHERE address_id < 500 AND first_name LIKE 'E%'
ORDER BY customer_id DESC
LIMIT 1;

-- 7. JOINS
-- California sales tax laws have changed and we need to alert our customers to this through email. What are the emails of the customers who live in California?

-- Counts addresses in California that are IDed 
SELECT COUNT(*) FROM address
WHERE district = 'California'
AND address_id IS NOT null;

-- Counts customers without addresses
SELECT COUNT(*) FROM customer
WHERE address_id IS null;

-- Selects emails (customer’s column) from join of address and customer table
-- Makes sure to join only address’s columns where district is California
-- LEFT, INNER or OUTER Joins will output same emails (since no adress_id row exists that isn’t in both tables)

SELECT email FROM address
INNER JOIN customer
ON address.address_id = customer.address_id
WHERE address.district = 'California';

-- A customer walks in and is a huge fan of the actor ‘Nick Wahlberg’ and wants to know which movies he is in. Get a list of all the movies ‘Nick Wahlberg’ has been in.

SELECT actor_id FROM actor
WHERE actor.first_name = ‘Nick’ AND actor.last_name = ‘Wahlberg’;

SELECT film.title FROM film
INNER JOIN film_actor
ON film_actor.film_id = film.film_id
WHERE film_actor.actor_id = 2;

-- Alternatively:

SELECT film_actor.film_id, film.title FROM film_actor
LEFT JOIN actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film_actor.film_id = film.film_id
WHERE actor.first_name = 'Nick' AND actor.last_name = 'Wahlberg';

-- During which months did payments occur? Format your answer to return back the full month name.

SELECT DISTINCT TO_CHAR(payment.payment_date,'Month') FROM payment;

-- How many payments occurred on a Monday?

SELECT COUNT(*) FROM payment
WHERE EXTRACT(ISODOW FROM payment_date) = 1;


-- Assessment Test 2

-- 1. How can you retrieve all the information from the cd.facilities table?
		SELECT * FROM cd.facilities;

-- 2. You want to print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs?

	SELECT name, membercost FROM cd.facilities;

-- 3. How can you produce a list of facilities that charge a fee to members?

SELECT * FROM cd.facilities
WHERE membercost != 0;

-- 4. How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.

SELECT facid, name, membercost, monthlymaintenance FROM cd.facilities
WHERE membercost != 0
AND membercost < monthlymaintenance/50;

-- 5. How can you produce a list of all facilities with the word 'Tennis' in their name?

SELECT * FROM cd.facilities
WHERE name LIKE '%Tennis%';

-- 6. How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.

SELECT * FROM cd.facilities
WHERE facid IN (1,5);

-- 7. How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question.

SELECT memid, surname, firstname, joindate FROM cd.members
WHERE EXTRACT(YEAR FROM joindate) = 2012
AND EXTRACT(MONTH FROM joindate) IN (09,10,11,12)

-- (or WHERE joindate >= '2012-09-01');

-- 8. How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.

SELECT DISTINCT surname FROM cd.members
ORDER BY surname
LIMIT 10;

-- 9. You'd like to get the signup date of your last member. How can you retrieve this information?

SELECT joindate FROM cd.members
ORDER BY joindate DESC
LIMIT 1;

-- (or MAX(joindate))


-- 10. Produce a count of the number of facilities that have a cost to guests of 10 or more.

SELECT COUNT(*) FROM cd.facilities
WHERE guestcost >= 10;

-- 11. Produce a list of the total number of slots booked per facility in the month of September 2012. Produce an output table consisting of facility id and slots, sorted by the number of slots.

SELECT facid, SUM(slots) AS TotalSlots FROM cd.bookings
WHERE EXTRACT(MONTH FROM starttime) = 09
GROUP BY facid
ORDER BY SUM(slots) ASC;

-- 12. Produce a list of facilities with more than 1000 slots booked. Produce an output table consisting of facility id and total slots, sorted by facility id.

SELECT facid, SUM(slots) AS TotalSlots FROM cd.bookings
GROUP BY facid
HAVING SUM(slots) >1000
ORDER BY facid ASC;

-- 13. How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.

SELECT bookings.starttime, facilities.name FROM cd.bookings
LEFT JOIN cd.facilities ON bookings.facid = facilities.facid
WHERE facilities.name LIKE '%Tennis Court%'
AND bookings.starttime >= '2012-09-21 00:00:00'::timestamp
AND bookings.starttime < '2012-09-22 00:00:00'::timestamp
ORDER BY bookings.starttime ASC;

-- 14. How can you produce a list of the start times for bookings by members named 'David Farrell'?

SELECT bookings.starttime, members.surname  FROM cd.bookings
LEFT JOIN cd.members ON bookings.memid = members.memid
WHERE members.firstname = 'David' AND members.surname = 'Farrell';