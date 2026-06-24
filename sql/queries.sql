SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

SELECT
strftime('%Y-%m', date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

SELECT
year,
AVG(yoy_growth_percent)
FROM monthly_sip_inflows
GROUP BY year;

SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

SELECT *
FROM fact_performance
WHERE expense_ratio < 1;