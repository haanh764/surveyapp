DROP PROCEDURE IF EXISTS add_allowed_respondent;
DELIMITER //
CREATE PROCEDURE add_allowed_respondent (IN respondentId int, IN surveyId int)    
BEGIN    
    DECLARE entry_exists int DEFAULT 0;  
    SELECT COUNT(*) INTO entry_exists FROM allowed_respondents 
    WHERE allowed_respondents.respondentId = respondentId 
        AND allowed_respondents.surveyId = surveyId;
    IF entry_exists = 0 THEN
        INSERT INTO `allowed_respondents`(`respondentId`, `surveyId`) VALUES (respondentId, surveyId);
    END IF;
END//
DELIMITER ;