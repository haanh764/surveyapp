--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `isActivated`, `isBlocked`) VALUES
(1, 'haanh.ngo764@gmail.com', 'sha256$mfvTMaqsLPw5q14v$6038078d50af9af5f7d9b070aa7f1f10df7882ffcf2493c32098e52575b1ad6e', 1, 0);

--
-- Dumping data for table `surveys`
--
INSERT INTO `surveys` (`id`, `surveyOwner`, `title`, `description`, `isPublic`, `surveyHash`, `isSurveySentAutomatically`, `isPublished`, `startDate`, `endDate`, `creationDate`, `modificationDate`) VALUES
(15, 1, 'Survey title', 'description', 1, NULL, NULL, 1, '2022-06-12 21:27:07', '2022-06-19 21:27:07', '2022-06-12 21:27:07', '2022-06-12 21:27:07'),
(16, 1, 'Mock Up Survey', NULL, 1, NULL, NULL, 1, '2022-06-12 21:27:07', '2022-06-19 21:27:07', '2022-06-12 21:27:07', '2022-06-12 21:27:07');

--
-- Dumping data for table `respondents`
--

INSERT INTO `respondents` (`id`, `email`) VALUES
(1, 'res1@gmail.com'),
(2, 'res2@gmail.com'),
(3, 'res3@gmail.com'),
(4, 'res4@gmail.com'),
(5, 'res5@gmail.com'),
(6, 'res6@gmail.com'),
(7, 'res7@gmail.com'),
(8, 'res8@gmail.com'),
(9, 'res9@gmail.com'),
(10, 'res10@gmail.com');

--
-- Dumping data for table `responses`
--

INSERT INTO `responses` (`id`, `surveyId`, `respondentId`) VALUES
(1, 16, 1),
(2, 16, 2),
(3, 16, 3),
(4, 16, 4),
(5, 16, 5),
(6, 16, 6),
(7, 16, 7),
(8, 16, 8),
(9, 16, 9),
(10, 16, 10);

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `surveyId`, `title`, `description`, `defaultValue`, `image`, `order_number`, `tag`, `model_key`, `model`) VALUES
(56, 16, 'Have you ever bought our product?', NULL, NULL, NULL, 1, NULL, '72b98a503', 'radio_72b98a503'),
(57, 16, 'How did you hear about our website?', NULL, NULL, NULL, 2, NULL, '5bc84abf1', 'checkbox_5bc84abf1'),
(58, 16, 'How satisfied are you?', NULL, NULL, NULL, 3, NULL, '6b457fb73', 'slider_6b457fb73'),
(59, 16, 'Do you have any comments on our products?', NULL, NULL, NULL, 4, NULL, 'e77197d15', 'input_e77197d15'),
(60, 16, 'How old are you?', NULL, NULL, NULL, 5, NULL, 'e77197d15', 'input_e77197d15');

--
-- Dumping data for table `scale_questions`
--
INSERT INTO `scale_questions` (`id`, `questionId`, `min_value`, `max_value`) VALUES
(14, 58, 1, 10);

--
-- Dumping data for table `open_answer_questions`
--

INSERT INTO `open_answer_questions` (`id`, `questionId`) VALUES
(3, 59),
(4, 60);

--
-- Dumping data for table `multiple_choice_questions`
--

INSERT INTO `multiple_choice_questions` (`id`, `questionId`, `allowMultipleAnswers`) VALUES
(15, 56, 0x00),
(16, 57, 0x01);


--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id`, `responseId`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);


--
-- Dumping data for table `scale_answers`
--
INSERT INTO `scale_answers` (`id`, `answerId`, `scale_question_id`, `value`) VALUES
(1, 1, 14, 4),
(2, 2, 14, 7),
(3, 3, 14, 9),
(4, 4, 14, 3),
(5, 5, 14, 8),
(6, 6, 14, 6),
(7, 7, 14, 9),
(8, 8, 14, 5),
(9, 9, 14, 7),
(10, 10, 14, 2);


--
-- Dumping data for table `open_answers`
--

INSERT INTO `open_answers` (`id`, `answerId`, `open_answer_question_id`, `answer_text`) VALUES
(1, 1, 4, '45'),
(2, 1, 3, 'Your products are good'),
(3, 2, 4, '23'),
(4, 2, 3, 'Easy to be broken, cheap quality'),
(5, 3, 4, '32'),
(6, 3, 3, 'Products are too expensive'),
(7, 4, 4, '25'),
(8, 4, 3, 'Low quality, hard to use'),
(9, 5, 4, '80'),
(10, 5, 3, 'Good prices, good quality'),
(11, 6, 4, '76'),
(12, 6, 3, 'Not good prices, low quality'),
(13, 7, 4, '48'),
(14, 7, 3, 'Product are good prices'),
(15, 8, 4, '37'),
(16, 8, 3, 'It is broken after delivery'),
(17, 9, 4, '28'),
(18, 9, 3, 'Products are too expensive'),
(19, 10, 4, '78'),
(20, 10, 3, 'The colors are not pretty, easy to fade away');

--
-- Dumping data for table `answer_options`
--

INSERT INTO `answer_options` (`id`, `multiple_choice_questions_id`, `image`, `text`) VALUES
(7, 15, NULL, 'Yes'),
(8, 15, NULL, 'No'),
(9, 16, NULL, 'Social Network'),
(10, 16, NULL, 'Website'),
(11, 16, NULL, 'Word-of-mouth'),
(12, 16, NULL, 'Television'),
(13, 16, NULL, 'Radio'),
(14, 16, NULL, 'Poster'),
(15, 16, NULL, 'Offline event');

--
-- Dumping data for table `choice_answers`
--


INSERT INTO `choice_answers` (`id`, `answerId`, `multiple_choice_questionsId`) VALUES
(1, 1, 15),
(2, 1, 16),
(3, 2, 15),
(4, 2, 16),
(5, 3, 15),
(6, 3, 16),
(7, 4, 15),
(8, 4, 16),
(9, 4, 16),
(10, 4, 16),
(11, 1, 16),
(12, 3, 16),
(13, 5, 15),
(14, 5, 16),
(15, 5, 16),
(16, 6, 15),
(17, 6, 16),
(18, 6, 16),
(19, 6, 16),
(20, 7, 15),
(21, 7, 16),
(22, 7, 16),
(23, 7, 16),
(24, 8, 15),
(25, 8, 16),
(26, 8, 16),
(27, 8, 16),
(28, 9, 15),
(29, 9, 16),
(30, 9, 16),
(31, 10, 15),
(32, 10, 16),
(33, 10, 16);

--
-- Dumping data for table `answer_options_choice_answer`
--

INSERT INTO `answer_options_choice_answer` (`id`, `choice_answerId`, `answer_optionId`) VALUES
(1, 1, 7),
(2, 2, 13),
(3, 3, 7),
(4, 4, 12),
(5, 5, 8),
(6, 6, 11),
(7, 7, 7),
(8, 8, 10),
(9, 9, 11),
(10, 10, 14),
(11, 11, 15),
(12, 12, 10),
(13, 13, 7),
(14, 14, 9),
(15, 15, 15),
(16, 16, 8),
(17, 17, 15),
(18, 18, 9),
(19, 19, 13),
(20, 20, 8),
(21, 21, 12),
(22, 22, 14),
(23, 23, 9),
(24, 24, 8),
(25, 25, 10),
(26, 26, 11),
(27, 27, 15),
(28, 28, 7),
(29, 29, 14),
(30, 30, 14),
(31, 31, 8),
(32, 32, 10),
(33, 33, 9);


--
-- Dumping data for table `surveys`
--
INSERT INTO `surveys` (`id`, `surveyOwner`, `title`, `description`, `isPublic`, `surveyHash`, `isSurveySentAutomatically`, `isPublished`, `startDate`, `endDate`, `creationDate`, `modificationDate`) VALUES
(17, 1, 'Mock Up Survey 2', NULL, 1, NULL, NULL, 1, '2022-06-12 21:27:07', '2022-06-19 21:27:07', '2022-06-12 21:27:07', '2022-06-12 21:27:07');


--
-- Dumping data for table `responses`
--

INSERT INTO `responses` (`id`, `surveyId`, `respondentId`) VALUES
(11, 17, 1),
(12, 17, 2),
(13, 17, 3),
(14, 17, 4),
(15, 17, 5),
(16, 17, 6),
(17, 17, 7),
(18, 17, 8),
(19, 17, 9),
(20, 17, 10);

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `surveyId`, `title`, `description`, `defaultValue`, `image`, `order_number`, `tag`, `model_key`, `model`) VALUES
(61, 17, 'Have you ever bought our product 2?', NULL, NULL, NULL, 1, NULL, '72b98a503', 'radio_72b98a503'),
(62, 17, 'How did you hear about our website 2?', NULL, NULL, NULL, 2, NULL, '5bc84abf1', 'checkbox_5bc84abf1'),
(63, 17, 'How satisfied are you? 2', NULL, NULL, NULL, 3, NULL, '6b457fb73', 'slider_6b457fb73'),
(64, 17, 'Do you have any comments on our products? 2', NULL, NULL, NULL, 4, NULL, 'e77197d15', 'input_e77197d15'),
(65, 17, 'How old are you? 2', NULL, NULL, NULL, 5, NULL, 'e77197d15', 'input_e77197d15');

--
-- Dumping data for table `scale_questions`
--
INSERT INTO `scale_questions` (`id`, `questionId`, `min_value`, `max_value`) VALUES
(15, 63, 1, 10);

--
-- Dumping data for table `open_answer_questions`
--

INSERT INTO `open_answer_questions` (`id`, `questionId`) VALUES
(5, 64),
(6, 65);

--
-- Dumping data for table `multiple_choice_questions`
--

INSERT INTO `multiple_choice_questions` (`id`, `questionId`, `allowMultipleAnswers`) VALUES
(17, 61, 0x00),
(18, 62, 0x01);


--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id`, `responseId`) VALUES
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20);


--
-- Dumping data for table `scale_answers`
--
INSERT INTO `scale_answers` (`id`, `answerId`, `scale_question_id`, `value`) VALUES
(11, 11, 15, 4),
(12, 12, 15, 7),
(13, 13, 15, 9),
(14, 14, 15, 3),
(15, 15, 15, 8),
(16, 16, 15, 6),
(17, 17, 15, 9),
(18, 18, 15, 5),
(19, 19, 15, 7),
(20, 20, 15, 2);


--
-- Dumping data for table `open_answers`
--

INSERT INTO `open_answers` (`id`, `answerId`, `open_answer_question_id`, `answer_text`) VALUES
(21, 11, 6, '45'),
(22, 11, 5, 'Your products are good'),
(23, 12, 6, '23'),
(24, 12, 5, 'Easy to be broken, cheap quality'),
(25, 13, 6, '32'),
(26, 13, 5, 'Products are too expensive'),
(27, 14, 6, '25'),
(28, 14, 5, 'Low quality, hard to use'),
(29, 15, 6, '80'),
(30, 15, 5, 'Good prices, good quality'),
(31, 16, 6, '76'),
(32, 16, 5, 'Not good prices, low quality'),
(33, 17, 6, '48'),
(34, 17, 5, 'Product are good prices'),
(35, 18, 6, '37'),
(36, 18, 5, 'It is broken after delivery'),
(37, 19, 6, '28'),
(38, 19, 5, 'Products are too expensive'),
(39, 20, 6, '78'),
(40, 20, 5, 'The colors are not pretty, easy to fade away');

--
-- Dumping data for table `answer_options`
--

INSERT INTO `answer_options` (`id`, `multiple_choice_questions_id`, `image`, `text`) VALUES
(16, 17, NULL, 'Yes'),
(17, 17, NULL, 'No'),
(18, 18, NULL, 'Social Network'),
(19, 18, NULL, 'Website'),
(20, 18, NULL, 'Word-of-mouth'),
(21, 18, NULL, 'Television'),
(22, 18, NULL, 'Radio'),
(23, 18, NULL, 'Poster'),
(24, 18, NULL, 'Offline event');

--
-- Dumping data for table `choice_answers`
--


INSERT INTO `choice_answers` (`id`, `answerId`, `multiple_choice_questionsId`) VALUES
(34, 11, 17),
(35, 11, 18),
(36, 12, 17),
(37, 12, 18),
(38, 13, 17),
(39, 13, 18),
(40, 14, 17),
(41, 14, 18),
(42, 14, 18),
(43, 14, 18),
(44, 11, 18),
(45, 13, 18),
(46, 15, 17),
(47, 15, 18),
(48, 15, 18),
(49, 16, 17),
(50, 16, 18),
(51, 16, 18),
(52, 16, 18),
(53, 17, 17),
(54, 17, 18),
(55, 17, 18),
(56, 17, 18),
(57, 18, 17),
(58, 18, 18),
(59, 18, 18),
(60, 18, 18),
(61, 19, 17),
(62, 19, 18),
(63, 19, 18),
(64, 20, 17),
(65, 20, 18),
(66, 20, 18);

--
-- Dumping data for table `answer_options_choice_answer`
--

INSERT INTO `answer_options_choice_answer` (`id`, `choice_answerId`, `answer_optionId`) VALUES
(34, 34, 7),
(35, 35 ,13),
(36, 36 ,7),
(37, 37 ,12),
(38, 38, 8),
(39, 39, 11),
(40, 40, 7),
(41, 41 ,10),
(42, 42 ,11),
(43, 43, 15),
(44, 44, 10),
(45, 45, 7),
(46, 46, 9),
(47, 47, 15),
(48, 48, 8),
(49, 49, 15),
(50, 50, 9),
(51, 51, 13),
(52, 52, 8),
(53, 53, 12),
(54, 54, 14),
(55, 55, 9),
(56, 56, 8),
(57, 57, 10),
(58, 58, 11),
(59, 59, 15),
(60, 60, 7),
(61, 61, 14),
(62, 62, 14),
(63, 63, 8),
(64, 64, 10),
(65, 65, 9),
(66, 66, 14);
