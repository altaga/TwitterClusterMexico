from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener



#consumer key, consumer secret, access token, access secret.
ckey= "YhwTUyeb4KWiUZEGRFUFfnNKP"
csecret="OVwSDj1Gt6ysFlmOI2VDyD5nvHLJ3zTpxwSHSp30wWLndR6yNP"
atoken="962558965761691648-etv8Xg7iSQXfKta1mB44mMR1N7jByVU"
asecret="OHWwWS23q4EPi6818khp2Syfp7wovbfSHWkJpLMuVQiyq"

F=0
n=0
class listener(StreamListener):
    def on_data(self, data):
        global F
        global n
        F=F+1
        #print("Unidades:" + str(F))
        if (F>10):
            F=0
            n=n+1
            print("Miles:" + str(n))
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(locations=[-117,18,-86,32],languages=["es"],track=["gol"])