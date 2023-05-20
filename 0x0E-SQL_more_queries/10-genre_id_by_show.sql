-- INNER JOIN MANIPULATIONS.

SELECT s.title, tv_show_genres.genre_id FROM tv_shows AS s INNER JOIN tv_show_genres ON s.id = tv_show_genres.show_id ORDER BY s.title ASC, tv_show_genres.genre_id ASC;
