SELECT e.name
FROM Employee AS e
JOIN Employee AS m
ON e.managerId = m.id
WHERE e.salary > m.salary;