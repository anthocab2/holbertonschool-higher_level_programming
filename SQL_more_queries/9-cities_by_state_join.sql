-- Lists all cities with their corresponding states.
-- Retrieves city id, city name and state name using one SELECT statement.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
