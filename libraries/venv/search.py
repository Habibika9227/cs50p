from artwork import get_artworks
from artist import get_artists
def main():
    art=input("Artwork: ")
    artists=get_artists(query=art, limit=3)
    for artist in artists:
        print(f"* {artist}")

main()