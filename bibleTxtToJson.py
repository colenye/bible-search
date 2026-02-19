import json
BIBLEFILE="translations/asv.txt"
d={}

with open(BIBLEFILE) as file:
    
    s = file.readline()
    while s:
       
        line = s.split('\t')
        book = line[0].rsplit(' ', 1)[0]
        chapterVerse = line[0].rsplit(' ', 1)[1]
        chapter = chapterVerse.split(':')[0]
        verse = chapterVerse.split(':')[1]
        content = line[1]
        s = file.readline()
    
        d.setdefault(book, {}).setdefault(chapter, {})[verse] = content
            

sep = BIBLEFILE.split('.')
newLine = sep[0] + ".json"
with open(newLine, "w") as file:
    json.dump(d, file, indent=4)