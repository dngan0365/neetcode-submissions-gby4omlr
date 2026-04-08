SELECT u.name, SUM(amount) balance
FROM users u
INNER JOIN transactions t ON u.account = t.account
GROUP BY u.account
HAVING SUM(amount) > 10000;

