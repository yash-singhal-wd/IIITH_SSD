SELECT CONCAT(Fname, " ", Lname) AS FULL_NAME, Ssn, Dno
FROM EMPLOYEE
WHERE Ssn IN (
    SELECT Mgr_ssn FROM DEPARTMENT
    Where Dnumber IN (
        SELECT Dno FROM EMPLOYEE
        Where Ssn IN (
            SELECT Essn FROM 
            (
            SELECT Essn,SUM(WORKS_ON.Hours) AS Hour_sum
            FROM WORKS_ON
            GROUP BY Essn
            ) AS T
            WHERE T.Hour_sum<40 OR T.Hour_sum IS NULL 
        )
    )
)