import songsingergenerator.music as music

def main():
    music.add_singer("Khalil Fong", "neosoul", ["Love Song", "SingalongSong"])
    print("Random Song:", music.random_song("neosoul"))
    print("Random Singer:", music.random_singer("rnb"))
    print("Find Singer:", music.find_singer("Pink"))

if __name__ == "__main__":
    main()
