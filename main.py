import json
import pandas as pd
import streamlit as st

word = "grace"
TRANSLATION = "translations/kjv.json"
st.title("Bible Search")
TRANSLATION = "translations/" + st.text_input("Enter the translation(kjv, esv etc.)") + ".json"


str = st.text_input("Enter words to search (case sensitive) ex: john,doe,roe or just joe")
words = str.split(',')

def summary(results: list):
    print("Word appears: " + str(len(results)) + " times.\n")


def occurences(word) -> list:
    results = []
    if word:
        with open(TRANSLATION, "r") as file:
            d = json.load(file)
            for book in d:
                for chapter in d[book]:
                    for verse in d[book][chapter]:
                        text = d[book][chapter][verse]
                        if word in text:
                            results.append((book, chapter, verse, text))
    return results
if words:
    results = []
    for c in words:
        occ = occurences(c)
        if occ:
            results.append(occurences(c))
    if results:
        lenResults = []
        for c in results:
            if c:
                lenResults.append(len(c))
        lenDf = pd.DataFrame({
            "results" : lenResults
        }, index=words)  
        st.bar_chart(lenDf)

        for index, c in enumerate(lenResults):
            st.write(f"Found **{c}** results for {words[index]}")

        lenDf = pd.DataFrame(lenResults)
        for index, result in enumerate(results):
            st.header(words[index])
            df = pd.DataFrame(result)

            if not df.empty and not lenDf.empty:
                st.dataframe(df)
                
            else:
                st.warning("no matches found")
        
        # Creates one big data frame of all words chosen
        st.header("All")
        df = pd.DataFrame(results)

        if not df.empty and not lenDf.empty:
            st.dataframe(df)
        else:
            st.warning("no matches found")
