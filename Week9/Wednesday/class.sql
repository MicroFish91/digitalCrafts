-- DROP TABLE album CASCADE;

-- CREATE TABLE album(
--     id serial PRIMARY KEY,
--     name VARCHAR,
--     year INTEGER,
--     artist_id INTEGER REFERENCES artist (id)
-- );

-- CREATE TABLE artist(
--     id serial PRIMARY KEY,
--     name VARCHAR
-- );

-- CREATE TABLE track(
--     id serial PRIMARY KEY,
--     name VARCHAR,
--     album_id INTEGER REFERENCES album (id),
--     duration TIME
-- );

-- INSERT INTO artist VALUES (
--     DEFAULT, 'Joe Biden'
-- );
