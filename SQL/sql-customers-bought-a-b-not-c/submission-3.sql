-- Find customers who purchased both products 'A' and 'B', 
-- but have never purchased product 'C'.
WITH ab_customers AS (
    -- Customers who bought A and B
    SELECT customer_id
    FROM orders
    WHERE product_name in ('A', 'B')
    GROUP BY customer_id
    HAVING 
        COUNT(DISTINCT product_name) = 2
),
c_customers AS (
    -- customers who have bought C
    SELECT DISTINCT(customer_id)
    FROM orders
    WHERE product_name = 'C'
)
SELECT c.customer_id, 
    c.customer_name
FROM customers c
JOIN ab_customers ab
    ON c.customer_id = ab.customer_id
LEFT JOIN c_customers cc
    ON ab.customer_id = cc.customer_id
WHERE cc.customer_id IS NULL
ORDER BY c.customer_name ASC;