-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name
FROM cities, states
WHERE statres_id = states.id
    AND states.name = 'California'
ORDER BY cities.id ASC;