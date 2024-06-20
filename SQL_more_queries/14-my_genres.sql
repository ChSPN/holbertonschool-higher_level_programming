-- This SQL statement uses the 'hbtn_0d_tvshows' database to list all genres of the show 'Dexter'.
-- The 'tv_shows' table contains only one record where 'title' = 'Dexter' (but the 'id' can be different).
-- Each record displays: 'tv_genres.name'.
-- The results are sorted in ascending order by the genre name.
-- Only one SELECT statement is used.
SELECT genres.name FROM genres JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = 'Dexter' ORDER BY genres.name ASC;
