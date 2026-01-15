import requests
import statistics
import json
import sys
if len(sys.argv)!=2:
    sys.exit()
# response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# o=response.json()
# for res in o["results"]:
#     print(res["trackName"])
print(statistics.mean(),+ sys.argv[1])

