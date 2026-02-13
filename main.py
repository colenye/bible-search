import json
import pandas as pd
word = "grace"

def summary(results: list):
    print("Word appears: " + str(len(results)) + " times.\n")



results = []
with open("kjv.json", "r") as file:
    d = json.load(file)
    for book in d:
        for chapter in d[book]:
            for verse in d[book][chapter]:
                text = d[book][chapter][verse]
                if word in text:
                    results.append((book, chapter, verse, text))
    df = pd.DataFrame(results)
for c in results:
    print(c)
summary(results)
        