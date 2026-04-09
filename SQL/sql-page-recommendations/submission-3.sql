-- Write your query below
SELECT DISTINCT page_id recommended_page
FROM likes
WHERE page_id NOT IN (
    SELECT page_id
    FROM LIKES
    WHERE user_id = 1
) AND user_id IN (
    SELECT user2_id AS user
    FROM friendship
    WHERE user1_id = 1
    UNION 
    SELECT user1_id AS user
    FROM friendship
    WHERE user2_id = 1
)
ORDER BY recommended_page;