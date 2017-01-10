# -*- coding: utf-8 -*-

import nltk
from matplotlib import style
from nltk import pos_tag
from nltk.tokenize import word_tokenize
#from nltk.chunk import conlltags2tree
from nltk.tree import Tree
#pip install langdetect daca nu este instalad modulul
from langdetect import detect
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
style.use('fivethirtyeight')


# Process text
def process_text():
    raw_text = open("sample_text.txt").read()
    token_text = word_tokenize(raw_text)
    return token_text

token_text=process_text()
tagged_words = nltk.pos_tag(token_text)

# NLTK POS and NER taggers

def nltk_tagger():
    ne_tagged = nltk.ne_chunk(tagged_words)
    return (ne_tagged)




# Parse named entities from tree
def structure_ne(ne_tree):
    ne = []
    for subtree in ne_tree:
        if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
            ne_label = subtree.label()
            ne_string = " ".join([token for token, pos in subtree.leaves()])
            ne.append((ne_string, ne_label))
    return ne

ne_tagged=structure_ne(nltk_tagger())

#Singura functie necesara pentru detectarea limbii(avand ca intrare un paragraf)
def get_language(paragraph):
    return detect(paragraph)
#Determinarea sinonimelor
def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None

def Synonym(tagged):

    synsets = [set() for _ in range(len(tagged))]
    lemmatzr = WordNetLemmatizer()
    for i,token in enumerate(tagged):
        wn_tag = penn_to_wn(token[1])
        target.write(token[0]+":")

        if not wn_tag:
            target.write('\n')
            continue
        lemma = lemmatzr.lemmatize(token[0], pos=wn_tag)
        for synonym in wn.synsets(lemma, pos=wn_tag):
            synsets[i].add(str(synonym)[8:-7])
        if(len(synsets[i])==0):
            synsets[i].add(lemma)
        target.write(str(synsets[i])[1:-1]+'\n')


#nltk_main()
target=open("output_text.txt", "w")
target.write("LANGUAGE:"+get_language(open("sample_text.txt").read())+"\n")
target.write("SYNONYMS:\n")
Synonym(tagged_words)

target.write("NAMED ENTITIES\n")
for i in ne_tagged:
    target.write(str(i)+"\n")
target.write("Words with POS TAG:\n")
for i in tagged_words:
    target.write(str(i)+"\n")
target.close()

