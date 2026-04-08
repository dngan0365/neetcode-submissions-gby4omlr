-- Write your query below
SELECT ct.name country
FROM person p
LEFT JOIN country ct ON SUBSTR(p.phone_number, 1, 3) = ct.country_code
LEFT JOIN calls c ON p.id = c.caller_id or p.id = c.callee_id
GROUP BY ct.name
HAVING AVG(c.duration) > (
    SELECT AVG(c.duration)
    FROM person p
    LEFT JOIN country ct ON SUBSTR(p.phone_number, 1, 3) = ct.country_code
    LEFT JOIN calls c ON p.id = c.caller_id or p.id = c.callee_id
)
