-- This SQL statement uses the 'hbtn_0d_tvshows' database to list all genres of the show 'Dexter'.
-- The 'tv_shows' table contains only one record where 'title' = 'Dexter' (but the 'id' can be different).
-- The results are sorted in ascending order by the genre name.
-- Only one SELECT statement is used.
SELECT tv_genres.name -- Select the genre name
FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id 
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id 
WHERE tv_shows.title = 'Dexter' 
ORDER BY tv_genres.name ASC;
