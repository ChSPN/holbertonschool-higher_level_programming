-- This SQL statement lists all Comedy shows in the 'hbtn_0d_tvshows' database.
-- The 'tv_genres' table contains only one record where 'name' = 'Comedy' (but the 'id' can be different).
-- Each record displays: 'tv_shows.title'.
-- The results are sorted in ascending order by the show title.
-- Only one SELECT statement is used.
SELECT
    tv_shows.title
FROM
    tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE
    tv_genres.name = 'Comedy'
ORDER BY
    tv_shows.title ASC;
