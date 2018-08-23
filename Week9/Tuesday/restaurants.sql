-- DROP TABLE restaurants;
-- DROP TABLE review;

-- -- CREATE TABLE restaurant(
-- --     id serial NOT NULL PRIMARY KEY,
-- --     name VARCHAR,
-- --     address VARCHAR,
-- --     category VARCHAR
-- -- );

-- -- CREATE TABLE reviewer(
-- --     id SERIAL NOT NULL PRIMARY KEY,
-- --     name VARCHAR,
-- --     email VARCHAR,
-- --     karma INTEGER CHECK (karma <= 7 and karma >= 0)
-- -- );

-- CREATE TABLE review(
--     id serial PRIMARY KEY,
--     title varchar,
--     review varchar,
--     stars integer check (stars >= 0 and stars <= 5),
--     reviewer_id integer REFERENCES reviewer (id),
--     restaurant_id integer REFERENCES restaurant (id)
-- );

-- INSERT INTO restaurant VALUES (
--     DEFAULT, 'RESTA', 'RESTADRESS', 'CAT-X'
-- );

-- INSERT INTO restaurant VALUES (
--     DEFAULT, 'RESTB', 'RESTBDRESS', 'CAT-X'
-- );

-- INSERT INTO restaurant VALUES (
--     DEFAULT, 'RESTC', 'RESTCDRESS', 'CAT-Y'
-- );

-- INSERT INTO restaurant VALUES (
--     DEFAULT, 'RESTD', 'RESTDDRESS', 'CAT-X'
-- );

-- INSERT INTO restaurant VALUES (
--     DEFAULT, 'RESTE', 'RESTEDRESS', 'CAT-Y'
-- );

-- INSERT INTO restaurant VALUES (
--     DEFAULT, 'RESTF', 'RESTFDRESS', 'CAT-Z'
-- );

-- INSERT INTO REVIEWER VALUES (
--     DEFAULT, 'GUYA', 'guya@gmail.com', 5
-- );

-- INSERT INTO REVIEWER VALUES (
--     DEFAULT, 'GUYB', 'guyb@gmail.com', 6
-- );

-- INSERT INTO REVIEWER VALUES (
--     DEFAULT, 'GUYC', 'guyc@gmail.com', 7
-- );

-- INSERT INTO REVIEWER VALUES (
--     DEFAULT, 'GUYD', 'guyd@gmail.com', 1
-- );

-- INSERT INTO REVIEWER VALUES (
--     DEFAULT, 'GALA', 'gala@gmail.com', 5
-- );

-- INSERT INTO REVIEWER VALUES (
--     DEFAULT, 'GALB', 'galb@gmail.com', 6
-- );

-- INSERT INTO REVIEWER VALUES (
--     DEFAULT, 'GALC', 'galc@gmail.com', 7
-- );

-- INSERT INTO REVIEWER VALUES (
--     DEFAULT, 'GALD', 'gald@gmail.com', 2
-- );

-- CREATE TABLE review(
--     id serial PRIMARY KEY,
--     title varchar,
--     review varchar,
--     stars integer check (stars >= 0 and stars <= 5),
--     reviewer_id integer REFERENCES reviewer (id), 8
--     restaurant_id integer REFERENCES restaurant (id) 6
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLEA', 'REVIEWBODYA', 3, 2, 4
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLEB', 'REVIEWBODYB', 2, 1, 4
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLEC', 'REVIEWBODYC', 5, 3, 4
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLED', 'REVIEWBODYD', 5, 1, 5
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLEE', 'REVIEWBODYE', 1, 4, 3
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLEF', 'REVIEWBODYF', 4, 5, 2
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLEG', 'REVIEWBODYG', 3, 6, 1
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLEH', 'REVIEWBODYH', 4, 7, 4
-- );

-- INSERT INTO review VALUES (
--     DEFAULT, 'TITLEI', 'REVIEWBODYI', 5, 7, 2
-- );




-- -- CREATE TABLE restaurant(
-- --     id serial NOT NULL PRIMARY KEY,
-- --     name VARCHAR,
-- --     address VARCHAR,
-- --     category VARCHAR
-- -- );

-- -- CREATE TABLE reviewer(
-- --     id SERIAL NOT NULL PRIMARY KEY,
-- --     name VARCHAR,
-- --     email VARCHAR,
-- --     karma INTEGER CHECK (karma <= 7 and karma >= 0)
-- -- );

-- CREATE TABLE review(
--     id serial PRIMARY KEY,
--     title varchar,
--     review varchar,
--     stars integer check (stars >= 0 and stars <= 5),
--     reviewer_id integer REFERENCES reviewer (id),
--     restaurant_id integer REFERENCES restaurant (id)
-- );

-- SELECT * FROM review where restaurant_id = 4;

-- SELECT * FROM restaurant
--     JOIN review ON review.restaurant_id = restaurant.id
--     where restaurant.name = 'RESTA';

-- SELECT * FROM reviewer
--     JOIN review on review.reviewer_id = reviewer.id
--     where reviewer.name = 'GUYA';

-- SELECT restaurant.name, review.review FROM review
    -- JOIN restaurant ON review.restaurant_id = restaurant.id
    -- JOIN reviewer ON review.reviewer_id = reviewer.id

-- SELECT restaurant.name, avg(review.stars) FROM review
--     JOIN restaurant ON review.restaurant_id = restaurant.id
--     GROUP BY restaurant.name;

-- SELECT restaurant.name, count(review.id) FROM review
--     JOIN restaurant ON review.restaurant_id = restaurant.id
--     GROUP BY restaurant.name;

-- SELECT restaurant.name, review.review, reviewer.name FROM review
--     JOIN restaurant ON review.restaurant_id = restaurant.id
--     JOIN reviewer ON review.reviewer_id = reviewer.id

-- SELECT reviewer.name, avg(review.stars) FROM review
--     JOIN reviewer ON review.reviewer_id = reviewer.id
--     GROUP BY reviewer.name

-- SELECT reviewer.name, min(review.stars) FROM review
--     JOIN reviewer ON review.reviewer_id = reviewer.id
--     GROUP BY reviewer.name

-- SELECT restaurant.category, count(restaurant.name) FROM restaurant GROUP BY restaurant.category;

-- SELECT restaurant.name, count(review.stars) FROM review
--     JOIN restaurant ON review.restaurant_id = restaurant.id
--     where review.stars = 5
--     GROUP BY restaurant.name;

