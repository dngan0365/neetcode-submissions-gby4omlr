-- Write your query below
SELECT DISTINCT ON (user_id)
    user_id,
    time_stamp AS last_stamp
FROM logins 
WHERE EXTRACT(YEAR FROM time_stamp::timestamp) = 2020
ORDER BY user_id, last_stamp DESC;