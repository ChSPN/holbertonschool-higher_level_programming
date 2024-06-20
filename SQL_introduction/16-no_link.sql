-- This SQL statement selects all records from 'second_table' where 'name' is not NULL.
-- Only the 'score' and 'name' fields are selected, in that order.
-- The results are ordered by 'score' in descending order.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
