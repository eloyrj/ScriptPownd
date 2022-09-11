from logging import exception
from pydoc import cli
import socket
import time
import tweepy
from tweepy import OAuthHandler




# Configuracion de acceso con las credenciales
consumer = "GCoxQyDK9ttrdCWJOKeSB1p6i"
consumerSecret = "SfZDtIluLr2rNP2I2pMeAfUuLd2o9wAYk0kCJrWHrEHMAZpi4C"
beared = "AAAAAAAAAAAAAAAAAAAAADYFbAEAAAAAJRHRK6hocpe0EpKAqTq982nhpO0%3DFYFdSX7MKMJpTwYiUdZmjuVdw1sKfTVeFLUmMidqQUIIJAIEQT"
access = "2942462098-fbhNJUS1A11SmNkqv8wXKcJrMBuuoJzc9B5KAns"
accessSecret = "dad7aeSWR77bLqYqzp7ec1y5gbJ6P9FXp3XBT0mxCKCOk"
clienID = "TklOMzJwOVg1UXhXRkpzUURMYU46MTpjaQ"
clienIDSecret = "RlzEdzuKBvukyLEKWBCzKGzrrUbgJ0S58VRPdY7-R_dXnVgA2t"

client = tweepy.Client(bearer_token=beared,consumer_key=consumer,consumer_secret=consumerSecret,access_token=access,access_token_secret=accessSecret)



HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65401 # The port used by the server

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(2000)
        d = str(data)[2:(len(str(data))-1)]
        print("Se ha recibido la id del Tweet procediendo con la respuesta, like y retweet: ... ")
        client.like(tweet_id=d)
        client.retweet(tweet_id=d)
        client.create_tweet(text="Que prueba tan chula",in_reply_to_tweet_id=d)
        print("like, Retweet y comentario realizado")
        s.close()
        time.sleep(33)



    