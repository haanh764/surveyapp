DROP TABLE IF EXISTS administrators;
DROP TABLE IF EXISTS allowed_respondents;
DROP TABLE IF EXISTS open_answers;
DROP TABLE IF EXISTS open_answer_questions;
DROP TABLE IF EXISTS scale_answers;
DROP TABLE IF EXISTS scale_questions;
DROP TABLE IF EXISTS choice_answers;
DROP TABLE IF EXISTS multiple_choice_questions;
DROP TABLE IF EXISTS answers;
DROP TABLE IF EXISTS responses;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS surveys;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS respondents;

CREATE TABLE administrators(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255),
    password varchar(255)
);

CREATE TABLE users (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255),
    password varchar(255)
);

CREATE TABLE respondents(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255)
);

CREATE TABLE surveys(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    surveyOwner int NOT NULL,
    title varchar(255),
    description varchar(255),
    startDate date,
    endDate date,
    creationDate date,
    modificationDate date,
    FOREIGN KEY (surveyOwner) REFERENCES users(id)
);

CREATE TABLE allowed_respondents(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    surveyId int NOT NULL,
    respondentId int NOT NULL,
    FOREIGN KEY (respondentId) REFERENCES respondents(id),
    FOREIGN KEY (surveyId) REFERENCES surveys(id) 
);

CREATE TABLE responses(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    surveyId int NOT NULL,
    respondentId int NOT NULL,
    FOREIGN KEY (respondentId) REFERENCES respondents(id),
    FOREIGN KEY (surveyId) REFERENCES surveys(id)
);

CREATE TABLE answers(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    responseId int NOT NULL,
    FOREIGN KEY (responseId) REFERENCES responses(id)
);

CREATE TABLE questions(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    surveyId int NOT NULL,
    title varchar(255),
    description varchar(255),
    image MEDIUMBLOB,
    FOREIGN KEY (surveyId) REFERENCES surveys(id)
);

CREATE TABLE open_answer_questions(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    questionId int NOT NULL,
    FOREIGN KEY (questionId) REFERENCES questions(id)
);

CREATE TABLE open_answers(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    answerId int NOT NULL,
    open_answer_question_questionId int NOT NULL,
    answer_text varchar(255),
    FOREIGN KEY (answerId) REFERENCES answers(id),
    FOREIGN KEY (open_answer_question_questionId) REFERENCES open_answer_questions(questionId)
);

CREATE TABLE scale_questions(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    questionId int NOT NULL,
    min_value float,
    max_value float,
    FOREIGN KEY (questionId) REFERENCES questions(id)
);

CREATE TABLE scale_answers(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    answerId int NOT NULL,
    scale_question_questionsId int NOT NULL,
    value int,
    FOREIGN KEY (scale_question_questionsId) REFERENCES scale_questions(questionId)
);

CREATE TABLE multiple_choice_questions(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    questionId int NOT NULL,
    allowMultipleAnswers binary(1),
    FOREIGN KEY (questionId) REFERENCES questions(id)
);

CREATE TABLE choice_answers(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    answerId int NOT NULL,
    multiple_choice_questions_questionId int NOT NULL,
    FOREIGN KEY (answerId) REFERENCES answers(id),
    FOREIGN KEY (multiple_choice_questions_questionId) REFERENCES multiple_choice_questions(questionId)
);