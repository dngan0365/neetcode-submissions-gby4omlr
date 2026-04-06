-- Write your query below
SELECT ROUND(AVG(
    CASE 
        WHEN customer_pref_delivery_date = order_date THEN 1
        ELSE 0
    END
)*100, 2) AS immediate_percentage
FROM delivery;