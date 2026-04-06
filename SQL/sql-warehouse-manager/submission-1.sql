-- Write your query below
SELECT w.name AS warehouse_name, SUM(w.units * p.width * p.length * p.height) AS volume
FROM warehouse AS w
INNER JOIN products AS p ON w.product_id = p.product_id 
GROUP BY w.name