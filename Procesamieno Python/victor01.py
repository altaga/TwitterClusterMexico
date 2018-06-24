from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import threading
import json
import sys


#consumer key, consumer secret, access token, access secret.
ckey='wA8uydwfmRDN6WEb18wEMY82J'
csecret='1nasUmp0Fx08LYWAHxEZL5DPKl2ruBOwEEtqtcJ6XvfaT9ABvx'
atoken='67507090-XHHWfMRcsxAyc55etUepM2yfWXjPnkkKdTBtpFlv9'
asecret='1Gdsaz8HEJM1X4f29Mgajh7N9ClAV8HUOHJQqH2xN9Fu2'

F=0
n=1
Mexico = [-117, 32, -86, 18]
tweet=""
guardar=""
numero=0
m=1
print("Hola")


class listener(StreamListener):
    def on_data(self, data):
        global F
        global n
        global m
        global numero
        global tweet
        global guardar
        all_data = json.loads(data)
        tweet = all_data["text"]
        guardar=guardar + tweet + ";;"
        #print(tweet)
        F=F+1
        print("Unidades:" + str(F))
        if (F>(10-1)):
            F=0
            numero=numero+1
            n=n+1
            File = open("AFDworkfile"+str(numero)+".txt",'w',encoding='utf-8')
            File.write(guardar)
            guardar=""
            File.close()
            if(n<6):
                n=1
                m=m+1
                if numero == 25:
                    sys.exit("Analisis Terminado")
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
print("Nuevo")
#aumentos horizontales .0880 y 1 ; -99.24, 19.27, -99.02, 19.52
twitterStream.filter(locations=[-99.23+n*0.0088, 19.26+m*0.01, -99.23+(n+1)*0.0088, 19.26+(m+1)*0.01],languages=["es"],track=["gol"])