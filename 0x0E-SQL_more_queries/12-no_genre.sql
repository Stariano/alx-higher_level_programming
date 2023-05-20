-- A script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT s.title, tv_show_genres.genre_id FROM tv_shows AS s LEFT OUTER JOIN tv_show_genres ON s.id = tv_show_genres.show_id WHERE tv_show_genres.show_id IS NULL ORDER BY s.title ASC, tv_show_genres.genre_id ASC;
