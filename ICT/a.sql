CREATE DATABASE ICT_Lab_3
CREATE TABLE companies (
    company_id INT PRIMARY KEY,
    company_name VARCHAR(255)
);

CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY,
    vehicle_type VARCHAR(255),
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE cities (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT
);

CREATE TABLE routes (
    route_id INT PRIMARY KEY,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

CREATE TABLE transport_types (
    transport_id INT PRIMARY KEY,
    transport_name VARCHAR(255),
    average_speed DECIMAL(5,2)
);

INSERT INTO companies VALUES
(1, 'AeroTrans'),
(2, 'Beta Logistics'),
(3, 'CargoPro'),
(4, 'DriveNow'),
(5, 'EcoLine');

INSERT INTO vehicles VALUES
(1, 'Truck', 2),
(2, 'Van', 2),
(3, 'Bus', 1),
(4, 'Electric Car', 5),
(5, 'Motorcycle', 4),
(6, 'SUV', 3);

INSERT INTO cities VALUES
(1, 'Almaty', 1),
(2, 'Astana', 1),
(3, 'Shymkent', 1),
(4, 'Tashkent', 2),
(5, 'Bishkek', 3);

INSERT INTO routes VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO transport_types VALUES
(1, 'Car', 80.00),
(2, 'Bus', 60.00),
(3, 'Truck', 70.00),
(4, 'Train', 110.00),
(5, 'Plane', 600.00);

--Task 1
SELECT c.company_name, COUNT(v.vehicle_id) AS vehicle_count
FROM companies c
LEFT JOIN vehicles v ON c.company_id = v.company_id
GROUP BY c.company_name;

--Task 2
SELECT * FROM companies
WHERE company_name LIKE 'A%';

--Task 3 
SELECT * FROM cities
WHERE country_id BETWEEN 3 AND 10;

--Task 4
SELECT vehicle_id, vehicle_type FROM vehicles;

--Task 5
SELECT r.route_id, c.city_name
FROM routes r
JOIN cities c ON r.city_id = c.city_id;

--Task 6 
SELECT * FROM transport_types;
UPDATE transport_types
SET average_speed = average_speed + 10
WHERE average_speed < 100;
SELECT * FROM transport_types;

--Task 7
SELECT city_name, country_id
FROM cities;

--Task 8 
SELECT transport_name FROM transport_types;
