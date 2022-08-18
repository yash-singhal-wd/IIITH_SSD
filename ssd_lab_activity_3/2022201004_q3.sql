SELECT Essn, COUNT(*) AS Number_of_Projects FROM WORKS_ON 
WHERE Essn IN 
(
    SELECT Mgr_ssn FROM DEPARTMENT
    WHERE Dnumber IN (
        SELECT Dnum 
        FROM PROJECT 
        WHERE Pname = "ProductY"
    )
)
GROUP BY Essn;