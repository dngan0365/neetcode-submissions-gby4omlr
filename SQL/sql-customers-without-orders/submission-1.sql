-- Write your query below
SELECT c.name
FROM customers as c
WHERE c.id NOT IN (
    SELECT o.customer_id
    FROM orders as o
)