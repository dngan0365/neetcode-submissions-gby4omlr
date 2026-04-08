-- Write your query below
SELECT DISTINCT c.title
FROM tv_program t
LEFT JOIN content c ON c.content_id = t.content_id
WHERE t.program_date LIKE '2020-06%'
        AND c.kids_content = 'Y' AND c.content_type = 'Movies';