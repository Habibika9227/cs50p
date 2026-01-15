import json
import requests
import sys

def main():
    o=sys.argv[1]
    try:
        response=requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q":o}
        )
    except requests.HTTPError:
        print("couldn't get the http request")
        return
    


    content=response.json()
    
    for art in content["data"]:
        print(f"*{art['title']}")
main()