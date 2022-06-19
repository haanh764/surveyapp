DROP TABLE IF EXISTS administrators;
DROP TABLE IF EXISTS allowed_respondents;
DROP TABLE IF EXISTS open_answers;
DROP TABLE IF EXISTS open_answer_questions;
DROP TABLE IF EXISTS scale_answers;
DROP TABLE IF EXISTS scale_questions;
DROP TABLE IF EXISTS answer_options_choice_answer;
DROP TABLE IF EXISTS answer_options;
DROP TABLE IF EXISTS choice_answers;
DROP TABLE IF EXISTS multiple_choice_questions;
DROP TABLE IF EXISTS answers;
DROP TABLE IF EXISTS responses;
DROP TABLE IF EXISTS question_analyses;
DROP TABLE IF EXISTS analyses;
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
    password varchar(255),
    isActivated boolean,
    isBlocked boolean
);

CREATE TABLE respondents(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) UNIQUE
);

CREATE TABLE surveys(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    surveyOwner int NOT NULL,
    title varchar(255),
    description varchar(255),
	isPublic boolean,
	surveyHash varchar(30),
	isSurveySentAutomatically boolean,
	isPublished boolean,
    startDate DATETIME,
    endDate DATETIME,
    creationDate DATETIME,
    modificationDate DATETIME,
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
    respondentId int,
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
	defaultValue varchar(255),
    image MEDIUMBLOB,
    order_number int,
    tag varchar(8),
    model_key varchar(255),
    model varchar(255),
    FOREIGN KEY (surveyId) REFERENCES surveys(id)
);

CREATE TABLE open_answer_questions(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	defaultValue varchar(255),
	placeholder varchar(255),
    questionId int NOT NULL,
    FOREIGN KEY (questionId) REFERENCES questions(id)
);

CREATE TABLE open_answers(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    answerId int NOT NULL,
    open_answer_question_id int NOT NULL,
    answer_text varchar(255),
    FOREIGN KEY (answerId) REFERENCES answers(id),
    FOREIGN KEY (open_answer_question_id) REFERENCES open_answer_questions(id)
);

CREATE TABLE scale_questions(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    questionId int NOT NULL,
	defaultValue float,
	step float,
    min_value float,
    max_value float,
    FOREIGN KEY (questionId) REFERENCES questions(id)
);

CREATE TABLE scale_answers(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    answerId int NOT NULL,
    scale_question_id int NOT NULL,
    value int,
    FOREIGN KEY (answerId) REFERENCES answers(id),
    FOREIGN KEY (scale_question_id) REFERENCES scale_questions(id)
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
    multiple_choice_questionsId int NOT NULL,
    FOREIGN KEY (answerId) REFERENCES answers(id),
    FOREIGN KEY (multiple_choice_questionsId) REFERENCES multiple_choice_questions(id)
);

CREATE TABLE analyses(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    creationDate DATETIME,
    surveyId int NOT NULL,
    FOREIGN KEY (surveyId) REFERENCES surveys(id)
);

CREATE TABLE question_analyses(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    data_type varchar(255),
    answer_count int,
    unique_answer_count int,
    modus int,
    median int,
    average float,
    most_frequent_answer varchar(255),
    least_frequent_answer varchar(255),
    most_frequent_answer_count int,
    least_frequent_answer_count int,
    analysisId int NOT NULL,
    questionId int NOT NULL,
    FOREIGN KEY (analysisId) REFERENCES analyses(id),
    FOREIGN KEY (questionId) REFERENCES questions(id)
);

CREATE TABLE answer_options(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    multiple_choice_questions_id int NOT NULL,
    image MEDIUMBLOB,
    text varchar(255),
	value_ varchar(255),
	defaultValue boolean,
    FOREIGN KEY (multiple_choice_questions_id) REFERENCES multiple_choice_questions(id)
);

CREATE TABLE answer_options_choice_answer(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    choice_answerId int NOT NULL,
    answer_optionId int NOT NULL,
    FOREIGN KEY (choice_answerId) REFERENCES choice_answers(id),
    FOREIGN KEY (answer_optionId) REFERENCES answer_options(id)
);
