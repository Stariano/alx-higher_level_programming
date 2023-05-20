-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS `number_of_shows` FROM tv_show_genres, tv_genres WHERE tv_show_genres.genre_id = tv_genres.id GROUP BY tv_show_genres.genre_id ORDER BY `number_of_shows` DESC;

