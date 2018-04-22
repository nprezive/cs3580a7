import re
import os
import string
from sklearn.feature_extraction import text

austen_words = list()
verne_words = list()
baum_words = list()


# Austen books
def mf_park():
    file = open('./Training/Austen/Mansfield_Park.txt', encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)                  #Set flags: x: "verbose" aka ignore comments and whitespace
                                                    #           s: "dotall" aka the dot char "." matches newlines
            (?<=(Produced\ by\ An\ Anonymous\ Volunteer))       #Lookbehind: Non-inclusive match
            (.*?)                                               #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jane Austen)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def n_abbey():
    file = open('./Training/Austen/Northanger_Abbey.txt', encoding='UTF-8')
    raw = file.read()
    file.close()

    pattern = re.compile(r'''(?xs)                  #Set flags: x: "verbose" aka ignore comments and whitespace
                                                    #           s: "dotall" aka the dot char "." matches newlines
            (?<=(Produced\ by\ An\ Anonymous\ Volunteer))       #Lookbehind: Non-inclusive match
            (.*?)                                               #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jane Austen)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def persuasion():
    file = open('./Training/Austen/Persuasion.txt', encoding='UTF-8')
    raw = file.read()
    file.close()

    pattern = re.compile(r'''(?xs)                  #Set flags: x: "verbose" aka ignore comments and whitespace
                                                    #           s: "dotall" aka the dot char "." matches newlines
            (?<=(HTML\ version\nby\ Al\ Haines))       #Lookbehind: Non-inclusive match
            (.*?)                                      #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jane Austen)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def pride_and_prejudice():
    file = open('./Training/Austen/Pride_and_Prejudice.txt', encoding='UTF-8')
    raw = file.read()
    file.close()

    pattern = re.compile(r'''(?xs)                  #Set flags: x: "verbose" aka ignore comments and whitespace
                                                    #           s: "dotall" aka the dot char "." matches newlines
            (PRIDE\ AND\ PREJUDICE:[\n\r]+A\ Novel\.[\n\r]+In\ Three\ Volumes.*?)    #Non-greedy match all
            (?=(Transcriber's\ note:[\n\r]+Spelling\ and\ hyphen\ changes\ have\ been\ made\ so\ that\ there))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jane Austen)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


# Verne books
def aatm():
    file = open('./Training/Verne/All_Around_the_Moon.txt', encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (ALL\n\nAROUND\ THE\ MOON\n\nFROM\ THE\ FRENCH\ OF.*?)   #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jules Verne)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def ftettm():
    file = open('./Training/Verne/From_the_Earth_to_the_Moon.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (FROM\ THE\ EARTH\ TO\ THE\ MOON,\ DIRECT\ IN\ NINETY-SEVEN\ HOURS\nAND\ TWENTY\ MINUTES:\ AND\ A\ TRIP\ ROUND\ IT:\n\nby\n\nJULES\ VERNE.*?)   #Non-greedy match all
            (?=(Transcriber's\ note:\n\nMinor\ inconsistencies\ in\ the\ spelling))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jules Verne)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def atwi8d():
    file = open('./Training/Verne/Around_the_World.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (AROUND\ THE\ WORLD\ IN\ EIGHTY\ DAYS\n\n\n\n
            CONTENTS\n\n\nCHAPTER.*?)   #Non-greedy match all
            (?=(End\ of\ Project\ Gutenberg's\ Around\ the\ World\ in\ 80\ Days))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jules Verne)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def jttcote():
    file = open('./Training/Verne/Journey_to_the_Centre_of_the_Earth.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (TABLE OF CONTENTS\n\n
            CHAPTER 1 MY UNCLE MAKES A GREAT DISCOVERY
            .*?)   #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of\ A\ Journey\ to\ the\ Centre\ of\ the\ Earth,\ by))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jules Verne)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


# Baum books
def datwio():
    file = open('./Training/Baum/Dorothy_and_the_Wizard_in_Oz.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (Dorothy\ and\ the\ Wizard\ in\ Oz\n\n\n
            \ \ A\ Faithful\ Record\ of\ Their\ Amazing\ Adventures
            .*?)   #Non-greedy match all
            (?=(End\ of\ Project\ Gutenberg's\ Dorothy\ and\ the\ Wizard\ in\ Oz,\ by))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(L. Frank Baum)|(Baum)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def tecoz():
    file = open('./Training/Baum/The_Emerald_City_of_Oz.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (The Emerald City of Oz\n\n\n
            by\n\n
            L.\ Frank\ Baum
            .*?)   #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of\ The\ Emerald\ City\ of\ Oz,\ by))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(L. Frank Baum)|(Baum)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def ooz():
    file = open('./Training/Baum/Ozma_of_Oz.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (Ozma\ of\ Oz\n\n
            \ \ A\ Record\ of\ Her\ Adventures\ with\ Dorothy\ Gale\ of\n\n\n
            .*?)   #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of\ Ozma\ of\ Oz,\ by))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(L. Frank Baum)|(Baum)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words


def twwoo():
    file = open('./Training/Baum/The_Wonderful_Wizard_of_Oz.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (The\ Wonderful\ Wizard\ of\ Oz\n\n\nby
            .*?)   #Non-greedy match all
            (?=(End\ of\ Project\ Gutenberg's\ The\ Wonderful\ Wizard\ of\ Oz,\ by))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(L. Frank Baum)|(Baum)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    words = raw.split()
    return words



austen_words.append(mf_park())
austen_words.append(n_abbey())
austen_words.append(persuasion())
austen_words.append(pride_and_prejudice())

verne_words.append(aatm())
verne_words.append(ftettm())
verne_words.append(atwi8d())
verne_words.append(jttcote())

baum_words.append(datwio())
baum_words.append(tecoz())
baum_words.append(ooz())
baum_words.append(twwoo())

print(baum_words[:9])





## Form bag of words model using words used at least 10 times
# vectorizer = text.CountVectorizer(min_df=10)
# X = vectorizer.fit_transform(papersH+papersM+papersD).toarray()
