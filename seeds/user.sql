-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, email, password) VALUES ('name', 'hello@gmail.com', '7a3d5ed42db8e77d91a838e6ad6b45cf68caf8e5aa5afbe0f65a0eceb431cafa')

-- testpassword1 (for hello@gmail.com)




