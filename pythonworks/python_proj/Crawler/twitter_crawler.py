__author__ = 'chengyu'


import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


consumer_key="OQrOsQkuiXFH5dUrCKHfvg"
consumer_secret="7pF6PH6PFGeBLlAHsxMbTGinw2bfYIw4aF6vwWsLok"


access_token="781737260-uJejBgaVA8NDGxj6oipjlp6K7fl89fvQdJQS6357"
access_token_secret="TZUCXTGg2SRBplHPaTs0aht2gGIsIwaRX1v6hBRSfJrzj"



fileDirectory = os.path.dirname(os.path.abspath(__file__))
fileDirectory = os.path.dirname(fileDirectory)
matrixFilePath = os.path.join(fileDirectory, "data/matrixForLearning")
dictFilePath = os.path.join(fileDirectory, "data/dictionary")

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

#
# class FileOutListener(StreamListener):
#     """
# A listener handles tweets are the received from the stream.
# This is a basic listener that just write received tweets to file.
# """
#
#     def __init__(self, fileName):
#         self.outPutFile = open(fileName,"w")
#
# #     def on_data(self, data):
# #         self.outPutFile.write(data+'\n')
#
#     def on_data(self, status):
#         self.outPutFile.write(status+'\n')






if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Cheng'])




