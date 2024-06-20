-- This SQL statement selects the 'score' and the number of records with the same 'score' from 'second_table'.
-- The number of records is labeled as 'number'.
-- The results are grouped by 'score' and ordered by 'number' in descending order.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
