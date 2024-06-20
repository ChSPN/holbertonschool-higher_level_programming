-- This SQL statement lists all shows contained in 'hbtn_0d_tvshows' that have at least one genre linked.
-- Each record displays: 'tv_shows.title' - 'tv_show_genres.genre_id'.
-- The results are sorted in ascending order by 'tv_shows.title' and 'tv_show_genres.genre_id'.
-- Only one SELECT statement is used.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres WHERE tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;