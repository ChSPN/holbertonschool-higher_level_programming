-- This SQL statement selects all records from 'second_table' where 'score' is greater than or equal to 10.
-- The results are ordered by 'score' in descending order.
-- Only the 'score' and 'name' fields are selected, in that order.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
