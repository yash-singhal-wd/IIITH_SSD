SELECT Dnumber, COUNT(*) AS Number_of_Locations
          FROM DEPT_LOCATIONS WHERE Dnumber IN ( 
              SELECT T2.Dnumber FROM 
              ( SELECT Dnumber, COUNT(*) AS Number_of_Deps FROM ( 
                  SELECT *
                  FROM DEPARTMENT
                  INNER JOIN DEPENDENT ON DEPARTMENT.Mgr_ssn = DEPENDENT.Essn
                  WHERE Sex='F'
              )AS T ) AS T2
              WHERE T2.Number_of_Deps >= 2
        );
