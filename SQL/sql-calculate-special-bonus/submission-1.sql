-- Calculate the bonus for each employee
-- bonus equal to salary if:
    -- employee_id is an odd number
    -- name does not start with the letter 'M'
-- else, bonus is 0
SELECT employee_id, 
    CASE
        WHEN employee_id % 2 = 1
        AND name NOT LIKE 'M%'
        THEN salary
        ELSE 0
    END AS bonus
FROM employees
ORDER BY employee_id ASC;