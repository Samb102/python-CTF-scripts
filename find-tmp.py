import requests
import sys

ext = [".backup", ".bck", ".old", ".save", ".bak", ".sav", "~", ".copy", ".old", ".orig",
        ".tmp", ".txt", ".back", ".bkp", ".bac", ".tar", ".gz", ".tar.gz", ".zip", ".rar"]

file = "index"

host = sys.argv[1]

for item in ext:
    try:
        url = host + item
        r = requests.get(url)
        print(url + " Code : " + str(r))
    except requests.exceptions.RequestException as e:
        if e.code == 404:
            print(url + " Code :  " + str(e))
        else:
            print(url + " Code :  " + str(e))
