DELIMITER //
CREATE PROCEDURE GetCustomConditionCustomers()
BEGIN
    SELECT T1.CUST_NAME, T1.GRADE FROM
    (
        SELECT CUST_NAME, GRADE, OPENING_AMT, RECEIVE_AMT, (OPENING_AMT + RECEIVE_AMT) AS AMOUNT_SUM
        FROM customer
    ) AS T1
    WHERE T1.AMOUNT_SUM>10000;
END //
DELIMITER ;

--CALL GetCustomConditionCustomers();
