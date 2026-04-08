-- Write your query below
SELECT date_id, make_name, COUNT(DISTINCT lead_id) unique_leads, COUNT(DISTINCT partner_id) unique_partners
FROM daily_sales d
GROUP BY date_id, make_name;