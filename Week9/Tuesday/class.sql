CREATE TABLE author (
    id serial PRIMARY KEY,
    name varchar
);

CREATE TABLE article (
    id serial PRIMARY KEY,
    title varchar,
    author_id integer REFERENCES author (id)
);

