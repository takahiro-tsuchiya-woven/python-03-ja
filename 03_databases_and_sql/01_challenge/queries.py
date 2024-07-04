
# SQLとPython＋Chinookデータベース

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# アーティストの数
def number_of_artists(db):
    query = "SELECT COUNT(DISTINCT Name) AS UniqueArtistCount FROM artists"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchone()
    return results[0]

# アーティストのリスト
def list_of_artists(db):
    query = "SELECT Name AS OrderedName FROM artists a ORDER BY Name ASC"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 「愛」をテーマにしたアルバムのリスト
def albums_about_love(db):
    # ここにSQLクエリを書いてください
    search_pattern = "%love%"
    query = """
        SELECT Title 
        FROM albums a 
        WHERE lower(Title) LIKE ?
        ORDER BY Title
    """
    db.execute(query, (search_pattern,))
    results = db.fetchall()
    return results

# 指定された再生時間よりも長い楽曲数
def tracks_longer_than(db, duration):
    query = """
        SELECT COUNT(Name)
        FROM tracks
        WHERE Milliseconds > ?
    """
    db.execute(query, (duration,))
    results = db.fetchone()
    return results[0]

# 最も楽曲数が多いジャンルのリスト
def genres_with_most_tracks(db):
    query = """
        SELECT
            g.Name AS GenreName,
            COUNT(t.TrackId) AS TrackCount
        FROM
            genres g 
        JOIN
            tracks t ON g.GenreId = t.GenreId
        GROUP BY
            g.Name
        ORDER BY
            TrackCount DESC
        LIMIT 1
    """
    db.execute(query)
    results = db.fetchall()
    return results

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()
