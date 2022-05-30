DROP PROCEDURE IF EXISTS add_response;
DELIMITER //
CREATE PROCEDURE add_response (IN respondentId int, IN surveyId int)    
BEGIN    
    DECLARE entry_exists int DEFAULT 0;  
    SELECT COUNT(*) INTO entry_exists FROM responses 
    WHERE responses.respondentId = respondentId 
        AND responses.surveyId = surveyId;
    IF entry_exists = 0 THEN
        INSERT INTO `responses`(`respondentId`, `surveyId`) VALUES (respondentId, surveyId);
    END IF;
END//
DELIMITER ;