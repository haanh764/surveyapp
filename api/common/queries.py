query_multiple_choices = "SELECT responses.id, respondents.email, questions.title, answer_options.text \
    FROM choice_answers JOIN answer_options_choice_answer ON choice_answers.id = answer_options_choice_answer.choice_answerId \
    JOIN multiple_choice_questions ON multiple_choice_questions.id = choice_answers.multiple_choice_questionsId \
    JOIN questions ON questions.id = multiple_choice_questions.questionId \
    JOIN answer_options ON answer_options.id = answer_options_choice_answer.answer_optionId \
    JOIN answers ON answers.id = choice_answers.answerId \
    JOIN responses ON answers.responseId = responses.id \
    JOIN respondents ON responses.respondentId = respondents.id \
    JOIN surveys ON surveys.id = responses.surveyId \
    WHERE surveys.id = %s"

query_open_answers = "SELECT responses.id, respondents.email, questions.title, open_answers.answer_text \
    FROM responses JOIN surveys ON surveys.id = responses.surveyId \
	JOIN respondents ON respondents.id = responses.respondentId \
    JOIN questions ON questions.surveyId = surveys.id \
    JOIN open_answer_questions ON open_answer_questions.questionId = questions.id \
    JOIN answers ON answers.responseId = responses.id \
    JOIN open_answers ON open_answers.open_answer_question_id = open_answer_questions.id and open_answers.answerId = answers.id \
    WHERE surveys.id = %s"

query_scale_answers = "SELECT responses.id, respondents.email, questions.title, scale_answers.value \
    FROM responses JOIN surveys ON surveys.id = responses.surveyId \
	JOIN respondents ON respondents.id = responses.respondentId \
    JOIN questions ON questions.surveyId = surveys.id \
    JOIN scale_questions ON scale_questions.questionId = questions.id \
    JOIN answers ON answers.responseId = responses.id \
    JOIN scale_answers ON scale_answers.scale_question_id = scale_questions.id and scale_answers.answerId = answers.id \
    WHERE surveys.id = %s"
    