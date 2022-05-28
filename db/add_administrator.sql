DROP PROCEDURE IF EXISTS add_administrator;
DELIMITER //
CREATE PROCEDURE add_administrator (IN admin_email VARCHAR(255), IN admin_password VARCHAR(255))    
BEGIN    
    DECLARE account_exists int DEFAULT 0;  
    SELECT COUNT(*) INTO account_exists FROM administrators WHERE administrators.email = admin_email;
    INSERT INTO `administrators`(`email`, `password`) VALUES (admin_email, admin_password);
END//
DELIMITER ;