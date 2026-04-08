-- Write your query below
SELECT o.customer_id, c.name
FROM orders o
LEFT JOIN product p ON o.product_id = p.product_id
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2020-06-1' AND o.order_date <= '2020-07-31'
GROUP BY o.customer_id, c.name
HAVING SUM(CASE 
                WHEN o.order_date >= '2020-06-1' AND o.order_date <= '2020-06-30'
                THEN o.quantity * p.price
                ELSE 0
                END)
             >= 100
        AND SUM(CASE 
                WHEN o.order_date >= '2020-07-1' AND o.order_date <= '2020-07-31'
                THEN o.quantity * p.price
                ELSE 0
                END)
             >= 100;