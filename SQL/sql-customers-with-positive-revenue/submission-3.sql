-- Write your query below
SELECT DISTINCT c.customer_id 
FROM customers AS c
WHERE c.year = 2020 AND c.revenue >0;