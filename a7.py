import re
import os
import string
from sklearn.feature_extraction import text
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB


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
    # words = raw.split()
    return raw


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
    # words = raw.split()
    return raw


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
    # words = raw.split()
    return raw


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
    # words = raw.split()
    return raw


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
    # words = raw.split()
    return raw


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
    # words = raw.split()
    return raw


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
    # words = raw.split()
    return raw


def jttcote():
    file = open('./Training/Verne/Journey_to_the_Centre_of_the_Earth.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (TABLE\ OF\ CONTENTS\n\n
            CHAPTER\ 1\ MY\ UNCLE\ MAKES\ A\ GREAT\ DISCOVERY
            .*?)   #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of\ A\ Journey\ to\ the\ Centre\ of\ the\ Earth,\ by))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(Jules Verne)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    # words = raw.split()
    return raw


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
    # words = raw.split()
    return raw


def tecoz():
    file = open('./Training/Baum/The_Emerald_City_of_Oz.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (The\ Emerald\ City\ of\ Oz\n\n\n
            by\n\n
            L.\ Frank\ Baum
            .*?)   #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of\ The\ Emerald\ City\ of\ Oz,\ by))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(L. Frank Baum)|(Baum)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    # words = raw.split()
    return raw


def ooz():
    file = open('./Training/Baum/Ozma_of_Oz.txt', 
            encoding='UTF-8')
    raw = file.read()
    file.close()
    pattern = re.compile(r'''(?xs)      #Set flags: 
                                        #x: "verbose" aka ignore comments and whitespace
                                        #s: "dotall" aka the dot char "." matches newlines
            (Ozma\ of\ Oz\n\n
            \ \ A\ Record\ of\ Her\ Adventures\ with\ Dorothy\ Gale\ of
            .*?)   #Non-greedy match all
            (?=(End\ of\ the\ Project\ Gutenberg\ EBook\ of\ Ozma\ of\ Oz,\ by))
        ''')

    m = re.search(pattern, raw)
    raw = m.group(0)

    raw = re.sub("('s)|[^a-zA-Z]|(L. Frank Baum)|(Baum)", " ", raw)
    raw = re.sub("\s+", " ", raw)
    # words = raw.split()
    return raw


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
    # words = raw.split()
    return raw


def readTestFile():
    success = False
    while not success:
        try:
            file_name = input('Please enter the file name of a book to predict:')
            file = open('./' + file_name)
            raw = file.read()
            file.close()
            success = True
            return raw
        except:
            print('File not found!')


corpus_data = [mf_park(), n_abbey(), persuasion(), pride_and_prejudice(),
          aatm(), ftettm(), atwi8d(), jttcote(),
          datwio(), tecoz(), ooz(), twwoo()]
corpus_target = [0,0,0,0,
                 1,1,1,1,
                 2,2,2,2]
corpus_target_names = ['Austen', 'Verne', 'Baum']


text_clf = Pipeline([('vect', text.CountVectorizer()),
                     ('tfidf', text.TfidfTransformer()),
                     ('clf', MultinomialNB()),
])

text_clf.fit(corpus_data, corpus_target)

repeat = True
while repeat:
    test_file = readTestFile()
    predicted = text_clf.predict([test_file])
    print("The author is... " + corpus_target_names[predicted[0]] + "!")

    while True:
        again = input("Another book?: (y/n) ")
        if again.lower() == 'y':
            break
        elif again.lower() == 'n':
            repeat = False
            break

