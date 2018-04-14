import re
import os
import string
from sklearn.feature_extraction import text

austen_words = list()
verne_words = list()
baum_words = list()

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

    pattern = re.compile(r'''(?xs)                            #Set flags: x: "verbose" aka ignore comments and whitespace
                                                                  #           s: "dotall" aka the dot char "." matches newlines

                    (?<=(Produced\ by\ An\ Anonymous\ Volunteer))       #Lookbehind: Non-inclusive match

                    (.*?)                                                 #Non-greedy match all

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
    print(raw)
    words = raw.split()
    return words



austen_words.append(mf_park())
austen_words.append(n_abbey())
austen_words.append(persuasion())
austen_words.append(pride_and_prejudice())

print(austen_words)




## Form bag of words model using words used at least 10 times
# vectorizer = text.CountVectorizer(min_df=10)
# X = vectorizer.fit_transform(papersH+papersM+papersD).toarray()