DROP TABLE IF EXISTS demo_listings;
DROP SEQUENCE IF EXISTS demo_listings_id_seq;
CREATE SEQUENCE IF NOT EXISTS demo_listings_id_seq;
CREATE TABLE demo_listings(
    id SERIAL PRIMARY KEY, title varchar(255), description text, price float, user_id int
);

INSERT INTO demo_listings (title, description, price, user_id) VALUES ('Forest & Heaven Themed Apartment in Melbourne', 'Located in the heart of CBD. Pretend you are lost in a magical forest as you perch on a log or curl up in the swinging chair /
Soak in the tub, then fall asleep in a heavenly bedroom with cloud-painted walls and twinkling lights, and when you wake up, the expresso machine waits.', 116, 1);
INSERT INTO demo_listings (title, description, price, user_id) VALUES ('Romantic, Stone House with Ocean Views', 'Located in Cape Town. Unwind at this stunning French Provencal beachside cotttage. The house was loveingly built with stone /
floors, high-beamed ceilings, and antinque details for a luxurious yet charming feel. Enjoy the sea and mountain views from the pool, lush garden and private patio leading off the living area.', 92, 1);
INSERT INTO demo_listings (title, description, price, user_id) VALUES ('Luxury City Centre Loft on a Traffic-Free Street', 'Located in Roma. Take an early morning stroll and enjoy the Trevi Fountain without the tourists. Wander / 
around the histoic streets wwile the city sleeps, then head back for a morning coffee at this urban-chic studio with a suspended loft bedroom.', 121, 1);
INSERT INTO demo_listings (title, description, price, user_id) VALUES ('Unique and Secluded AirShip with Breathtaking Highland Views', 'Located in Drimnin. Retreat to the deck of this sustainable getaway and gaze at the twinkling constellations under a tartan blanket. AirShip 2 is an iconic, insulated aluminum pod /
with views of the Sound of Mull from dragonfly windows. The AirShip 2 is comfotable, quirky and cool.', 170, 1);