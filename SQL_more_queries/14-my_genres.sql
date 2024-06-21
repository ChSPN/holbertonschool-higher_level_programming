-- This SQL statement uses the 'hbtn_0d_tvshows' database to list all genres of the show 'Dexter'.
-- The 'tv_shows' table contains only one record where 'title' = 'Dexter' (but the 'id' can be different).
-- The results are sorted in ascending order by the genre name.
-- Only one SELECT statement is used.
SELECT tv_genres.name -- Select the genre name
FROM tv_shows
    -- Join the tv_shows table with the tv_show_genres table on the show_id
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
    -- Join the tv_show_genres table with the tv_genres table on the genre_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'-- Filter the results to include only the show titled "Dexter"
ORDER BY tv_genres.name ASC;-- Sort the results in ascending order by the genre name
