-- This SQL statement lists all genres from 'hbtn_0d_tvshows' and displays the number of shows linked to each.
-- Each record displays: '<TV Show genre>' - '<Number of shows linked to this genre>'.
-- The first column is called 'genre' and the second column is called 'number_of_shows'.
-- Genres that don’t have any shows linked are not displayed.
-- The results are sorted in descending order by the number of shows linked.
-- Only one SELECT statement is used.
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM genres JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id GROUP BY genres.name HAVING COUNT(tv_show_genres.show_id) > 0 ORDER BY COUNT(tv_show_genres.show_id) DESC;
