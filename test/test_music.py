import songsingergenerator.music as music

def test_add_singer():
    music.add_singer("Test Singer", "pop", ["Song A", "Song B"])
    assert "pop" in music.collection
    assert "Test Singer" in music.collection["pop"]
    assert "Song A" in music.collection["pop"]["Test Singer"]

def test_random_song():
    music.add_singer("Test Singer", "pop", ["Song A"])
    result = music.random_song("pop")
    assert result is not None
    assert result[0] == "Test Singer"
    assert result[1] == "Song A"

def test_random_singer():
    music.add_singer("Test Singer", "pop")
    assert music.random_singer("pop") == "Test Singer"

def test_find_singer():
    music.add_singer("Test Artist", "pop")
    assert ("Test Artist", "pop") in music.find_singer("Test")

def test_random_song_no_songs():
    music.add_singer("Empty Singer", "jazz", [])
    assert music.random_song("jazz") is None
