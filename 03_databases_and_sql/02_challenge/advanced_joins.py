
# SQLとPython＋Chinookデータベース: 高度な結合

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# 楽曲の詳細
def detailed_tracks(db):
    query = """
        SELECT t.Name, a1.Title, a2.Name 
        FROM tracks t 
        LEFT OUTER JOIN albums a1
        ON t.AlbumId = a1.AlbumId 
        LEFT OUTER JOIN artists a2
        ON a1.ArtistId = a2.ArtistId
    """  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 未購入の楽曲
def tracks_not_bought(db):
    query = """
        SELECT t.Name 
        FROM tracks t
        LEFT OUTER JOIN invoice_items ii 
        ON t.TrackId = ii.TrackId 
        WHERE ii.TrackId is NULL 
        ORDER by t.Name
    """  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# ジャンルの統計情報
def genre_stats(db, genre_name):
    query = """
        SELECT
            g.Name,
            COUNT(t.TrackId) AS number_of_tracks,
            AVG(t.Milliseconds / 1000.0) AS avg_track_length
        FROM
            genres g
        JOIN
            tracks t ON g.GenreId = t.GenreId
        WHERE
            g.Name = ?
        GROUP BY
            g.Name
    """  # ここにSQLクエリを書いてください
    db.execute(query, (genre_name,))
    results = db.fetchone()
    print(results)
    if results:
        return {
            'genre': results[0],
            'number_of_tracks': results[1],
            'avg_track_length': results[2]
        }
    else:
        return None

# ジャンル別のトップ5アーティスト
def top_five_artists_by_genre(db, genre_name):
    query = """
    SELECT artists.Name AS artist_name, COUNT(tracks.TrackId) AS number_of_tracks
    FROM genres
    JOIN tracks ON genres.GenreId = tracks.GenreId
    JOIN albums ON tracks.AlbumId = albums.AlbumId
    JOIN artists ON albums.ArtistId = artists.ArtistId
    WHERE genres.Name = ?
    GROUP BY artists.Name
    ORDER BY number_of_tracks DESC, artists.Name ASC
    LIMIT 5
    """  # ここにSQLクエリを書いてください
    db.execute(query, (genre_name,))
    results = db.fetchall()
    return results

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()
