import nltk
import os
import threading
import json
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import numpy
from es_nlp import stem
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
global nbclassifier
global known_words
import es_nlp as lang_tools


#Geolocalizacion del area de interes
ckey = "YhwTUyeb4KWiUZEGRFUFfnNKP"
csecret = "OVwSDj1Gt6ysFlmOI2VDyD5nvHLJ3zTpxwSHSp30wWLndR6yNP"
atoken = "962558965761691648-etv8Xg7iSQXfKta1mB44mMR1N7jByVU"
asecret = "OHWwWS23q4EPi6818khp2Syfp7wovbfSHWkJpLMuVQiyq"




#Base de datos de identificacion de sentimientos

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



#Inicio geografico 


#Obtencion de tweets

F=0
n=1
Mexico = [-117, 32, -86, 18]
tweet=""
guardar=""
numero=0
m=1
exp_count=0;
exp_value=0;
radios=numpy.zeros(25)

class listener(StreamListener):
    def on_data(self, data):
        global F
        global n
        global m
        global numero
        global tweet
        global guardar
        global exp_count
        global exp_value
        global radios
        all_data = json.loads(data)
        tweet = all_data['text']
        if  not all_data['text'].startswith('RT'):
            guardar=guardar + tweet + ";"
            all_data=""
            data=""
            tweet=""
            #print(tweet)
            F=F+1
        else:
            all_data=""
            data=""
            tweet=""
        if (F>(10-1)):
            F=0
            n=n+1
            exp_count=0;
            exp_value=0;
            tokens=lang_tools.tokenize(guardar)
            guardar=""
            numero=numero+1
            print(radios)
            for e in tokens:
                if e in known_words:
                    exp_count=exp_count+1
                    sentiment=nbclassifier.classify(extract_feature(e))
                    exp_value+=float(sentiment)-1
            if exp_count > 0:
                    scale_sentiment=exp_value/exp_count
                    acceptance=(scale_sentiment/2)*(100)
                    radios[numero-1]=1-(acceptance/300)
            else:
                    acceptance=0	
                    radios[numero-1]=1-(acceptance/300)
        if(n<6):
            n=1
            m=m+1
            if numero == 25:
                n=1
                m=1
                numero=1
                File = open("/var/www/html/xml/radios.xml",'w')
                File.write("<datos>")
                for i in range(0,25):
                    File.write("<id> " + str(radios[i]) + "</id>")
                File.write("</datos>")
                File.close()
                print(radios)
        return(True)


    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
#aumentos horizontales .0880 y 1 ; -99.24, 19.27, -99.02, 19.52
twitterStream.filter(locations=[-99.23+(n)*0.0088, 19.26+(m)*0.01, -99.23+(n+1)*0.0088, 19.26+(m+1)*0.01],languages=["es"],track=["e"])