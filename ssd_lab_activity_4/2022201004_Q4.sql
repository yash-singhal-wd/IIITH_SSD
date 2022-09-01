DELIMITER //
CREATE PROCEDURE GettingCustomerWithAgent()
BEGIN
    DECLARE c_name varchar(100);
    DECLARE c_city varchar(100);
    DECLARE c_country varchar(100);
    DECLARE c_grade int;
    DECLARE v_finish int default 0;
    DECLARE cur_1 cursor for SELECT CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE FROM customer WHERE AGENT_CODE LIKE 'A00%';
    DECLARE CONTINUE handler for not found set v_finish=1;
    open cur_1;
    the_loop:loop
    fetch cur_1 into c_name, c_city, c_country, c_grade;
    Select c_name, c_city, c_country, c_grade;
    if v_finish=1 then
    leave the_loop;
    end if;
    end loop the_loop; 
END //
DELIMITER ;

--CALL GettingCustomerWithAgent();