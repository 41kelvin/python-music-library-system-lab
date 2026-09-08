from song import Song


def fresh_library():
    class Library(Song):
        count = 0
        artists = []
        genres = []
        genre_count = {}
        artists_count = {}
        artist_count = {}

    return Library


def test_repeated_artists_and_genres():
    library = fresh_library()
    library('Halo', 'Beyonce', 'Pop')
    library('Love on Top', 'Beyonce', 'Pop')
    library('99 Problems', 'Jay Z', 'Rap')

    assert library.count == 3
    assert library.artists == ['Beyonce', 'Jay Z']
    assert library.genres == ['Pop', 'Rap']
    assert library.genre_count == {'Pop': 2, 'Rap': 1}
    assert library.artists_count == {'Beyonce': 2, 'Jay Z': 1}
    assert library.artist_count == library.artists_count


def test_class_methods_without_creating_song():
    library = fresh_library()
    for _ in range(2):
        library.add_song_to_count()
        library.add_to_artists('Beyonce')
        library.add_to_genres('Pop')
        library.add_to_genre_count('Pop')
        library.add_to_artists_count('Beyonce')

    assert library.count == 2
    assert library.artists == ['Beyonce']
    assert library.genres == ['Pop']
    assert library.genre_count == {'Pop': 2}
    assert library.artists_count == {'Beyonce': 2}
    assert library.artist_count == {'Beyonce': 2}
