DELIMITER //
CREATE PROCEDURE GetCustomersByCity(
    IN  cityName varchar(40)
)
BEGIN
    SELECT CUST_NAME 
    FROM customer
    WHERE WORKING_AREA = cityName;
END //
DELIMITER ;

--CALL GetCustomersByCity('Bangalore');


