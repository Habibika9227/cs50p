import statistics
import sys
import cowsay
import requests
# if len(sys.argv)!=3:
#    sys.exit("too few arguments")
# print(statistics.mean(), + sys.argv[1])

# for arg in sys.argv[1:]:
#    print("hello, world", arg)
response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
