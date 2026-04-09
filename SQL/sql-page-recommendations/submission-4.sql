-- Write your query below
SELECT DISTINCT page_id recommended_page
FROM likes
WHERE page_id NOT IN (
    SELECT page_id
    FROM LIKES
    WHERE user_id = 1
) AND user_id IN (
    SELECT GREATEST(user1_id, user2_id) AS user
    FROM friendship
    WHERE LEAST(user1_id, user2_id) = 1
)
ORDER BY recommended_page;