--Which one of below Queries are right?

--Number 1
SELECT CustomerID, count(*) as order_count FROM [Orders] WHERE order_count > 5
GROUP BY CustomerID
ORDER BY order_count desc


--Number 2
SELECT CustomerID, count(*) AS order_count FROM Orders
GROUP BY CustomerID HAVING order_count > 5
ORDER BY order_count DESC

--Note: If the condition is on aggregation function use HAVING
--When using aggregate functions (COUNT, SUM, MAX, ...) you cant just use
--WHERE after SELECT, because the aggregate function is not processed until
--GROUP BY has done, so you have to use HAVING operator in aggregate functions
--for implementing conditions
--Number 2 is correct

SELECT CustomerID, count(*) AS order_count FROM Orders WHERE CDate > '1990-01-01'
GROUP BY CustomerID HAVING order_count > 5
ORDER BY order_count DESC
