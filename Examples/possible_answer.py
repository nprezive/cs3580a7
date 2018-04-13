from __future__ import division
import numpy as np
import json
from sklearn.feature_extraction import text


x = open('fedpapers_split.txt').read()
papers = json.loads(x)

papersH = papers[0] # papers by Hamilton 
papersM = papers[1] # papers by Madison
papersD = papers[2] # disputed papers

nH, nM, nD = len(papersH), len(papersM), len(papersD)

# This allows you to ignore certain common words in English
# You may want to experiment by choosing the second option or your own
# list of stop words, but be sure to keep 'HAMILTON' and 'MADISON' in
# this list at a minimum, as their names appear in the text of the papers
# and leaving them in could lead to unpredictable results
stop_words = text.ENGLISH_STOP_WORDS.union({'HAMILTON','MADISON'})
#stop_words = {'HAMILTON','MADISON'}

## Form bag of words model using words used at least 10 times
vectorizer = text.CountVectorizer(stop_words=stop_words,min_df=10)
X = vectorizer.fit_transform(papersH+papersM+papersD).toarray()

# Uncomment this line to see the full list of words remaining after filtering out 
# stop words and words used less than min_df times
print(vectorizer.vocabulary_)

# Split word counts into separate matrices
XH, XM, XD = X[:nH,:], X[nH:nH+nM,:], X[nH+nM:,:]

# Estimate probability of each word in vocabulary being used by Hamilton
fH = []
k = XH.sum(axis=0)
total_sum = sum(k)

for i in range(0,len(XH[1])):
    prob = ((k[i] + 1)/(float(total_sum + len(XH[1]))))
    fH.append(prob)
    

# Estimate probability of each word in vocabulary being used by Madison
fM = []
k = XM.sum(axis=0)
total_sum = sum(k)

for i in range(0,len(XM[1])):
    prob = ((k[i] + 1)/float(total_sum + len(XM[1])))
    fM.append(prob)
    

# Compute ratio of these probabilities
#fratio = fH/fM
fratio = [a/b for a,b in zip(fH,fM)]

# Compute prior probabilities 
piH = len(XH)/float(len(X))
piM = len(XM)/float(len(X))

for xd in range(0,len(XD)): # Iterate over disputed documents
    # Compute likelihood ratio for Naive Bayes model
    tmp = [np.power(a,b) for a,b in zip(fratio,XD[xd])]
    tmp = np.prod(np.array(tmp))
    LR = tmp*(piH)/(piM)
    if LR>0.5:
        print('Hamilton')
    else:
        print('Madison')

