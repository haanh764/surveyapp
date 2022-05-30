DROP PROCEDURE IF EXISTS add_respondent;
DELIMITER //
CREATE PROCEDURE add_respondent (IN respondent_email VARCHAR(255))    
BEGIN    
    DECLARE account_exists int DEFAULT 0;  
    SELECT COUNT(*) INTO account_exists FROM respondents WHERE respondents.email = respondent_email;
    IF account_exists = 0 THEN
        INSERT INTO `respondents`(`email`) VALUES (respondent_email);
    END IF;
END//
DELIMITER ;