import json
import pandas as pd
import streamlit as st

checkDfs = []
word = "grace"
TRANSLATION = "translations/kjv.json"
st.title("Bible Search")
translations = st.text_input("Enter the translation(kjv,asv,cpdv,jps)").split(',')
TRANSLATIONS = []
for index in range(len(translations)):
    TRANSLATIONS.append(translations[index])
    translations[index] = "translations/" + translations[index] + ".json"


str = st.text_input("Enter words to search (case sensitive) ex: john,doe,roe or just joe")
words = str.split(',')
check = st.text_input("Translation Check (case sensitive)")
columns = st.columns(len(translations))

def occurences(word) -> list:
            results = []
            if word:
                with open(translations[index], "r") as file:
                    d = json.load(file)
                    for book in d:
                        for chapter in d[book]:
                            for verse in d[book][chapter]:
                                text = d[book][chapter][verse]
                                if word in text:
                                    results.append((book, chapter, verse, text))
            return results


for index, column in enumerate(columns):
    with column:
        st.title(TRANSLATIONS[index])
        def summary(results: list):
            print("Word appears: " + str(len(results)) + " times.\n")

        if words:
            results = []
            total = []
            for c in words:
                occ = occurences(c)
                if occ:
                    results.append(occ)
                total.append(occ)
            if results:
                lenResults = []
                for c in results:
                    if c:
                        lenResults.append(len(c))
                
                wordle = []
                for i in range (len(total)):
                    if len(total[i]) > 0:
                        wordle.append(words[i])
                lenDf = pd.DataFrame({
                    "results" : lenResults
                }, index=wordle) 
                st.bar_chart(lenDf)
                
        

                for index, c in enumerate(lenResults):
                    st.write(f"Found **{c}** results for {words[index]}")

                # Creates data frame for each word
                lenDf = pd.DataFrame(lenResults)
                for index, result in enumerate(results):
                    if words[index] == check:
                        checkDfs.append(result)


                    st.header(wordle[index])
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
st.header("Super All")
st.dataframe(checkDfs)
#Index of the highest word occurence of all translations
lensOfCheckDfs = []
for c in checkDfs:
    lensOfCheckDfs.append(len(c))
verseComp = []
if lensOfCheckDfs:
    largestLen = max(lensOfCheckDfs)
    indexOfLargestLen = lensOfCheckDfs.index(largestLen)
    print(indexOfLargestLen)

    for index, translation in enumerate(TRANSLATIONS):
        trans = []
        with open(translations[index], "r") as file:
            file = json.load(file)
            for c in range(largestLen):
                # this gets the translation with the largest amount of occurences of chosen word
                tup = checkDfs[indexOfLargestLen][c]
                book = tup[0]
                chapter = tup[1]
                verse = tup[2]
                trans.append((book, chapter, verse, file[book][chapter][verse]))
        verseComp.append(trans)

st.header("Comparison (Shows the each translation with the same number of verses as highest one)")
st.dataframe(verseComp)
