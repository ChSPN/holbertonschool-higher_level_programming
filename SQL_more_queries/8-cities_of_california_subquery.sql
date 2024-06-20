-- This SQL statement lists all the cities of California that can be found in the database 'hbtn_0d_usa'.
-- The results are sorted in ascending order by 'cities.id'.
-- The 'JOIN' keyword is not used. Instead, a subquery is used to get the 'id' of the state 'California' from the 'states' table.
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
