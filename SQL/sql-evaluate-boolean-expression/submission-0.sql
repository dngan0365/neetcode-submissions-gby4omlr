-- Write your query below
SELECT e.left_operand, e.operator, e.right_operand,
    CASE
        WHEN e.operator = '>' AND lv.value > rv.value THEN true
        WHEN e.operator = '<' AND lv.value < rv.value THEN true
        WHEN e.operator = '=' AND lv.value = rv.value THEN true
        ELSE false
    END AS value
FROM expressions e
INNER JOIN variables lv ON e.left_operand = lv.name
INNER JOIN variables rv ON e.right_operand = rv.name;