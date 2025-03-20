import random

collection = {
    "rnb": {
        "SZA": ["Luther", "30 For 30", "Snooze", "Kill Bill", "Good Days"],
        "Babyface": ["Every Time I Close My Eyes", "Lady, Lady", "Illusions", "When Can I See You Again"],
        "Alicia Keys": ["No One", "If I Ain't Got You", "Fallin'"],
        "Beyoncé": ["Irreplaceable", "Halo", "Drunk in Love"]
    },
    "rock": {
        "Pink Floyd": ["Wish You Were Here", "Comfortably Numb", "Time", "Shine On You Crazy Diamond"],
        "The Beatles": ["Come Together", "Here Comes The Sun", "Hey Jude", "Let It Be"],
        "The Rolling Stones": ["Paint It Black", "Gimme Shelter", "Sympathy for the Devil"],
        "Led Zeppelin": ["Stairway to Heaven", "Whole Lotta Love", "Kashmir"]
    },
    "hip-hop": {
        "Kendrick Lamar": ["HUMBLE.", "Alright", "Money Trees", "DNA."],
        "Drake": ["God's Plan", "In My Feelings", "One Dance", "Hotline Bling"],
        "J. Cole": ["No Role Modelz", "Love Yourz", "Wet Dreamz"],
        "Kanye West": ["Stronger", "Gold Digger", "Flashing Lights"]
    },
    "pop": {
        "Taylor Swift": ["Blank Space", "Love Story", "You Belong With Me", "Shake It Off"],
        "Adele": ["Hello", "Someone Like You", "Rolling in the Deep", "Set Fire to the Rain"],
        "Ed Sheeran": ["Shape of You", "Thinking Out Loud", "Perfect"],
        "Dua Lipa": ["Don't Start Now", "Levitating", "New Rules"]
    },
    "jazz": {
        "Miles Davis": ["So What", "Freddie Freeloader", "Blue in Green"],
        "John Coltrane": ["Giant Steps", "My Favorite Things", "Blue Train"],
        "Louis Armstrong": ["What a Wonderful World", "La Vie En Rose", "Stardust"],
        "Ella Fitzgerald": ["Summertime", "Cheek to Cheek", "Dream a Little Dream of Me"]
    },
    "country": {
        "Johnny Cash": ["Ring of Fire", "Hurt", "Folsom Prison Blues"],
        "Dolly Parton": ["Jolene", "9 to 5", "Coat of Many Colors"],
        "Willie Nelson": ["On the Road Again", "Always on My Mind", "Blue Eyes Crying in the Rain"],
        "Luke Combs": ["Beautiful Crazy", "Hurricane", "Beer Never Broke My Heart"]
    },
    "electronic": {
        "Daft Punk": ["One More Time", "Get Lucky", "Harder, Better, Faster, Stronger"],
        "Calvin Harris": ["Summer", "Feel So Close", "This Is What You Came For"],
        "Deadmau5": ["Strobe", "Ghosts 'n' Stuff", "Some Chords"],
        "Zedd": ["Clarity", "Stay", "The Middle"]
    },
    "classical": {
        "Ludwig van Beethoven": ["Symphony No. 9", "Für Elise", "Moonlight Sonata"],
        "Wolfgang Amadeus Mozart": ["Eine kleine Nachtmusik", "Requiem", "The Magic Flute"],
        "Johann Sebastian Bach": ["Toccata and Fugue in D Minor", "Brandenburg Concerto", "Air on the G String"],
        "Pyotr Ilyich Tchaikovsky": ["Swan Lake", "The Nutcracker", "1812 Overture"]
    }
}

def add_singer(singer, genre, songs=None):
    """Add a singer with songs to the collection under a specific genre."""
    if songs is None:
        songs = []
    genre = genre.lower()
    if genre not in collection:
        collection[genre] = {}
    if singer in collection[genre]:
        collection[genre][singer].extend(songs)
    else:
        collection[genre][singer] = songs

def random_song(genre=None):
    """Return a random song from a given genre or any genre if not specified."""
    if genre:
        genre = genre.lower()
        if genre not in collection or not collection[genre]:
            return None
        singers = list(collection[genre].keys())
        chosen_singer = random.choice(singers)
        songs = collection[genre][chosen_singer]
        if not songs:
            return None
        return (chosen_singer, random.choice(songs), genre)
    else:
        if not collection:
            return None
        chosen_genre = random.choice(list(collection.keys()))
        return random_song(chosen_genre)

def random_singer(genre=None):
    """Return a random singer from a given genre or any genre if not specified."""
    if genre:
        genre = genre.lower()
        if genre not in collection or not collection[genre]:
            return None
        return random.choice(list(collection[genre].keys()))
    else:
        if not collection:
            return None
        chosen_genre = random.choice(list(collection.keys()))
        return random_singer(chosen_genre)

def find_singer(keyword):
    """Find singers whose name contains the given keyword (case insensitive)."""
    keyword = keyword.lower()
    result = []
    for genre, singers in collection.items():
        for singer in singers.keys():
            if keyword in singer.lower():
                result.append((singer, genre))
    return result
