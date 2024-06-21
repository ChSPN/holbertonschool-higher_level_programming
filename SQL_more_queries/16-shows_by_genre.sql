-- Ce script SQL liste tous les spectacles et tous les genres liés à ce spectacle, à partir de la base de données 'hbtn_0d_tvshows'.
-- Si un spectacle n'a pas de genre, 'NULL' est affiché dans la colonne du genre.
-- Chaque enregistrement affiche : 'tv_shows.title' - 'genres.name'.
-- Les résultats sont triés par ordre croissant par le titre du spectacle et le nom du genre.
-- Seule une instruction SELECT est utilisée.
SELECT
    tv_shows.title,
    tv_genres.name
FROM
    tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = genres.id
ORDER BY
    tv_shows.title ASC,
    tv_genres.name ASC;
