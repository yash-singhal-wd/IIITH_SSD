DELIMITER //
CREATE PROCEDURE addTwoNums(
    IN num1 INT, IN num2 INT, OUT res INT
)
BEGIN
    SELECT num1 + num2 
    INTO res;

    SELECT res AS Sum_Result;
END //
DELIMITER ;

-- CALL addTwoNums(45,24,@res);