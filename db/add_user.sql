DROP PROCEDURE IF EXISTS add_user;
DELIMITER //
CREATE PROCEDURE add_user (IN user_email VARCHAR(255), IN user_password VARCHAR(255))    
BEGIN   
    DECLARE account_exists int DEFAULT 0;  
    SELECT COUNT(*) INTO account_exists FROM users WHERE users.email = user_email;
    IF account_exists = 0 THEN
        INSERT INTO `users`(`email`, `password`) VALUES (user_email, user_password);
    END IF;
END//
DELIMITER ;