
import sqlite3
from queries import *

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# number_of_artistsのテスト
def test_number_of_artists():
    assert number_of_artists(db) > 0, "The number of artists should be greater than 0."

# list_of_artistsのテスト
def test_list_of_artists():
    artists = list_of_artists(db)
    assert isinstance(artists, list), "Should return a list."
    assert len(artists) > 0, "The list of artists should not be empty."

# albums_about_loveのテスト
def test_albums_about_love():
    albums = albums_about_love(db)
    assert isinstance(albums, list), "Should return a list."
    for album in albums:
        assert 'love' in album[0].lower(), "Each album title should contain 'love'."

# tracks_longer_thanのテスト
def test_tracks_longer_than():
    duration = 200000  # 200 seconds
    count = tracks_longer_than(db, duration)
    assert isinstance(count, int), "Should return an integer."
    assert count > 0, "There should be tracks longer than the given duration."

# genres_with_most_tracksのテスト
def test_genres_with_most_tracks():
    genres = genres_with_most_tracks(db)
    assert isinstance(genres, list), "Should return a list."
    assert len(genres) > 0, "The list of genres should not be empty."
    prev_count = float('inf')
    for genre, count in genres:
        assert count <= prev_count, "Genres should be ordered by descending track count."
        prev_count = count

# テストを実行
test_number_of_artists()
test_list_of_artists()
test_albums_about_love()
test_tracks_longer_than()
test_genres_with_most_tracks()

print("All tests passed!")
