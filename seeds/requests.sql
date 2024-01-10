
DROP TABLE IF EXISTS requests;

DROP SEQUENCE IF EXISTS requests_id_seq;

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;

CREATE TABLE requests(

    id SERIAL PRIMARY KEY, 
    date_from date, 
    date_to date,
    user_id int,
    listing_id int,
    confirmed boolean
);

-- ONCE THIS IS READY REFERENECE THE USER ID
INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES (2024-01-10, 2024-01-17, 1, 1, True);
INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES (2024-02-02, 2024-02-06, 2, 1, True);
