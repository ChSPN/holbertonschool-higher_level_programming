-- This SQL statement lists all genres from 'hbtn_0d_tvshows' and displays the number of shows linked to each.
-- Each record displays: '<TV Show genre>' - '<Number of shows linked to this genre>'.
-- The first column is called 'genre' and the second column is called 'number_of_shows'.
-- Genres that don’t have any shows linked are not displayed.
-- The results are sorted in descending order by the number of shows linked.
-- Only one SELECT statement is used.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
-- Join the tv_genres table with the tv_show_genres table
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
-- Only include genres that have at least one show
HAVING COUNT(tv_show_genres.show_id) > 0
-- Order the results by the number of shows in each genre, from most to least
ORDER BY number_of_shows DESC;
