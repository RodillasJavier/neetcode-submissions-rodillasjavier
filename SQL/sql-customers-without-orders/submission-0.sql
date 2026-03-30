-- Write a query to find all customers who have never placed an order. 
-- Return the customer names. 
-- The result can be returned in any order.
SELECT customers.name
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
WHERE orders.customer_id IS NULL;