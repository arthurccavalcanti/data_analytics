-- 1. Analyst Builder - Tech Layoffs
-- Write a query to determine the percentage of employees that were laid off from each company. Output should include the company and the percentage (to 2 decimal places) of laid off employees. Order by  company name alphabetically.

SELECT company, ROUND((employees_fires/company_size)*100),2) AS Percentage
FROM tech_layoffs
ORDER BY company ASC;

-- 2. Separation
-- Data was input incorrectly into the database. The ID was combined with the First Name. Write a query to separate the ID and First Name into two separate columns. Each ID is 5 characters long.

SELECT
	SUBSTRING(id,1,5) AS new_id
	SUBSTRING(id,6) AS first_name
FROM bad_data;

-- 2. Kelly’s 3rd Purchase
/*
Kelly gives a 33% discount on each customer’s 3rd purchase
Write a query to select the 3rd transaction for each customer that received that discount.
Output the customer id, transaction, amount, and the amount after the discount as discounted_amount
Order output on customer id in ascending order.
*/

WITH cte1 AS
(
SELECT *, ROW_NUMBER() OVER(PARTITION BY customer_id
ORDER BY transaction_id) AS row_num
FROM purchases
)
SELECT customer_id, transaction_id, amount, (amount*0.67) AS discounted_amount FROM cte1
WHERE cte1.row_num = 3
ORDER BY customer_id ASC;

-- 3. Temperature Fluctuations
-- Write a query to find all dates with higher temperatures compared to the previous dates (yesterday). Order dates in ascending order.

SELECT t1.temperature
FROM temperature AS t1
JOIN temperature AS t2
	ON DATEDIFF(t1.date,t2.date) = 1
	AND t1.temperature > t2. temperature
ORDER BY t1.date;