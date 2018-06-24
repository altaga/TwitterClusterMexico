import es_nlp as lang_tools
import nltk
import pickle
import os
from es_nlp import stem
global nbclassifier
global known_words

classifier_file="clasificador.pickle"
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


#Para evitar crear y entrenar el clasificador una y otra vez 
# usamos pickle para grabar el objeto entrenado como archivo binario
if not (os.path.isfile(classifier_file)):
	nbclassifier = nltk.NaiveBayesClassifier.train(feature_set)
	f = open(classifier_file, 'wb')
	pickle.dump(nbclassifier, f)
	f.close();
else:
	f = open(classifier_file, 'rb')
	nbclassifier = pickle.load(f)
	f.close()



print("Ingresa una frase para el proceso de NLP:")
t=input();
print(lang_tools.tokenize(t));

import es_nlp as lang_tools
from clasificador import nbclassifier,known_words,extract_feature

print("Ingrese una frase para el análisis:")
t=input()
exp_count=0;
exp_value=0;

tokens=lang_tools.tokenize(t)
for e in tokens:
	if e in known_words:
		exp_count+=1
		sentiment=nbclassifier.classify(extract_feature(e))
		exp_value+=float(sentiment)-1
if exp_count>0:
	scale_sentiment=exp_value/exp_count
	acceptance=scale_sentiment/2*100 
	print("Valor de Sentimiento: "+str(scale_sentiment+1))
	print("Aceptacion: "+str(acceptance)+"%")
	
else:
	print("No se pudo determinar")
	acceptance=0
	
valor=1-(acceptance/300)