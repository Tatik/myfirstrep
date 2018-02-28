CREATE TABLE passengers (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  flight_id INTEGER REFERENCES flights );


INSERT INTO passengers (name, flight_id) VALUES ('Alice',1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob',1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie',1);
INSERT INTO passengers (name, flight_id) VALUES ('Dave',2);
INSERT INTO passengers (name, flight_id) VALUES ('Elen',2);
INSERT INTO passengers (name, flight_id) VALUES ('Frank',4);
INSERT INTO passengers (name, flight_id) VALUES ('Julian',5);
INSERT INTO passengers (name, flight_id) VALUES ('Beatrice',6);
INSERT INTO passengers (name, flight_id) VALUES ('Timothy',7);
