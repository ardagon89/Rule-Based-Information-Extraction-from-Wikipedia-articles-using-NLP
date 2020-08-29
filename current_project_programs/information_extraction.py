import spacy
import numpy as np
import pandas as pd
import os
import stopwords
from current_project_programs.preprocess import Preprocess
from nltk.parse.stanford import StanfordParser
nlp = spacy.load('en_core_web_sm')

def load_text_files(dir='../dataset/'):
    list_of_directory = os.listdir(dir)
    data = []
    for file in list_of_directory:
        current = open(dir+file,"r",encoding='ISO-8859-1')
        list_of_sentences = []
        for count, line in enumerate(current):
            list_of_sentences.append(line.strip())
        data.append(list_of_sentences)
    dataset = pd.DataFrame({"sentences":data})
    return dataset


dataset = load_text_files()
prep = Preprocess()
for doc_index in range(len(dataset)):
    for line_index in range(len(dataset["sentences"][doc_index])):
        current_sentence = dataset["sentences"][doc_index][line_index]
        current_sentence =  prep.remove_unwanted_character(current_sentence).lstrip()
        current_sentence = prep.sentence_tokenize(current_sentence)
        for each_sent in current_sentence:
            lem_sent = prep.lemmatize(each_sent)
            cleaned_sentence = prep.remove_stopwords(lem_sent)
            cleaned_sentence = prep.word_tokenize(cleaned_sentence)
            cleaned_sentence = prep.pos_tag(cleaned_sentence)
            print(cleaned_sentence)
    exit()









