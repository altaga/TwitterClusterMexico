import es_nlp as lang_tools
import nltk
import pickle
import os
import threading
import json
import sys
from es_nlp import stem
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
global nbclassifier
global known_words

lexicon_ord="meanAndStdev.csv"

def extract_feature(w):
	return {"word":w}


# funcion que construye el set para entrenamiento del algoritmo clasificador
# lexico para el entrenamiento
lexicon_lines=open(lexicon_ord,"r", encoding='utf-8').readlines();
labeled_words=[]
known_words=[]
for line in lexicon_lines:
	split=line.replace("\n","").split(";")
	word=split[0].split("_")
	word=stem(word[0])
	known_words.append(word)
	labeled_words.append((word,split[1]))
feature_set=[(extract_feature(n), sentiment) for (n, sentiment) in labeled_words]
nbclassifier = nltk.NaiveBayesClassifier.train(feature_set)

adi="workfile25.txt";
adi_lines=str(open(adi,"r", encoding='utf-8').readlines());
exp_count=0;
exp_value=0;



tokens=lang_tools.tokenize(adi_lines)
for e in tokens:
	if e in known_words:
		exp_count+=1
		sentiment=nbclassifier.classify(extract_feature(e))
		exp_value+=float(sentiment)-1
if exp_count>0:
	scale_sentiment=exp_value/exp_count
	acceptance=scale_sentiment/2*100 
		
else:
	acceptance=0
	
valor=1-(acceptance/300)