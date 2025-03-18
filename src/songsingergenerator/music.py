import random
collection = {
    "rnb":{
        "SZA":["luther", "30 For 30", "Snooze", "Kill Bill"],
        "Babyface" : ["Every Time I close my Eyes", "Lady, Lady", "Illusions"]        
    },
    "rock":{
        "Pink Floyd":["Wish You Were Here", "comfortably Numb", "Time"],
        "The Beatles":["Come Togethers", "Here Comes The Sun", "Here, There And EveryWhere"]
    }
}

def addSinger(singer, genre, songs=None):
    #note here we need to pass genre as well not only singer
    if songs is None:
        songs = []
    genre = genre.lower()
    if genre not in collection:
        collection[genre] = {}
    if singer in collection[genre]:
        collection[genre][singer].extend(songs)
    else:
        collection[genre][singer] = songs
def randomSong(genre=None):
    if genre:
        genre = genre.lower()
        if genre not in collection or not collection[genre]:
            return None
        singersL = list(collection[genre].keys())
        chosenSinger = random.choice(singersL)
        songsL = collection[genre][chosenSinger]
        if not songsL:
            return None
        chosenSong = random.choice(songsL)
        return (chosenSinger, chosenSong, genre)
    else:
        if not collection:
            return None
        Genres = list(collection.keys())
        chosenGenre = random.choice(Genres)
        #call itself but pass the genre
        return randomSong(chosenGenre)
def randomSinger(genre = None):
    if genre:
        genre = genre.lower()
        if genre not in collection or not collection[genre]:
            return None
        singerL = list(collection[genre].keys())
        return random.choice(singerL)
    else:
        if not collection:
            return None
        Genres = list(collection.keys())
        chosenGenre = random.choice(Genres)
        return randomSinger(chosenGenre)
def findSinger(inWord):
    inWord = inWord.lower()
    result = []
    for genre, singers in collection.items():
        for singer in singers.keys():
            if inWord in singer.lower():
                result.append((singer, genre))
    return result
    
        
        
    