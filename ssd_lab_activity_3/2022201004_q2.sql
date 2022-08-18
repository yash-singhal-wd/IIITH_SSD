SELECT CONCAT(Fname, " ", Lname) AS FULL_NAME, Ssn, Dno  
FROM EMPLOYEE CROSS Apply (
    SELECT Super_ssn, COUNT(*)
    FROM EMPLOYEE
    WHERE Super_ssn IS NOT NULL
    GROUP BY Super_ssn
)
WHERE Ssn IN ;