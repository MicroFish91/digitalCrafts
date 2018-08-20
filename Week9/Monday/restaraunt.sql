-- CREATE TABLE restaraunt (
--     id SERIAL NOT NULL PRIMARY KEY, 
--     name varchar,
--     distance real,
--     stars integer,
--     category varchar,
--     favoriteDish varchar,
--     doesTakeout boolean,
--     lastTimeAte date
-- );

-- INSERT INTO restaraunt VALUES (
--     DEFAULT, 'RestarauntOne', 5.32, 4, 'Fusion', 'Chicken', TRUE, '2016-02-04'
-- );

-- INSERT INTO restaraunt VALUES (
--     DEFAULT, 'RestarauntTwo', 2.12, 3, 'HomeStyle', 'Beef', TRUE, '2017-01-02'
-- );

-- INSERT INTO restaraunt VALUES (
--     DEFAULT, 'RestarauntThree', 1.35, 5, 'Sushi', 'Fish', FALSE, '2017-02-04'
-- );

-- INSERT INTO restaraunt VALUES (
--     DEFAULT, 'RestarauntFour', 0.92, 2, 'Fake', 'Nothing', FALSE, '2018-02-04'
-- );

-- INSERT INTO restaraunt VALUES (
--     DEFAULT, 'RestarauntFive', 3.13, 3, 'Basic', 'Bland', TRUE, '2018-03-06'
-- );

-- INSERT INTO restaraunt VALUES (
--     DEFAULT, 'RestarauntFive', 2.13, 5, 'Exquisite', 'Sashimi', FALSE, '2017-05-06'
-- );

-- SELECT name FROM restaraunt where stars = 5;

-- SELECT favoriteDish FROM restaraunt where stars = 5;

-- SELECT id FROM restaraunt where name = 'RestarauntThree';

-- SELECT name FROM restaraunt where category = 'Sushi';

-- SELECT name FROM restaraunt where doesTakeout = TRUE;

-- SELECT name FROM restaraunt where doesTakeout = TRUE and category = 'HomeStyle';

-- SELECT name FROM restaraunt where distance < 2;

-- SELECT name FROM restaraunt where lastTimeAte >= '2018-02-03' and lastTimeAte <= '2018-02-11';

-- SELECT name FROM restaraunt ORDER BY distance;

-- SELECT name FROM restaraunt ORDER BY distance LIMIT 2; 

-- SELECT COUNT(*) FROM restaraunt;

-- SELECT COUNT(name), category FROM restaraunt GROUP BY category;

-- SELECT category, AVG(stars) FROM restaraunt GROUP BY category;

SELECT category, MAX(stars) FROM restaraunt GROUP BY category;