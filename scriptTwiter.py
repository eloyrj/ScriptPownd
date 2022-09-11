
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



    
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65401  # Port to listen on (non-privileged ports are > 1023)
query = 'from:cortecerito26'
id = 2942462098

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        
        idnueva=idantigua = client.get_users_tweets(id=id).meta.get("newest_id")
        
        
        while True:    
            dnueva=idantigua = client.get_users_tweets(id=id).meta.get("newest_id")
            print("Esperando conexxion con el Bot")
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"conectado a {addr} Esperando a un nuevo tweet")
                
                
                while(idnueva==idantigua):
                    
                    time.sleep(30)
                    idnueva = client.get_users_tweets(id=id).meta.get("newest_id")
                
                
                print("Tweet nuevo reconocido, con id: ",idnueva," Trasmitiendo ....")
                conn.sendall(bytes(str(idnueva), 'utf8'))
                time.sleep(30)
except KeyboardInterrupt :
    print()
finally:
    s.close()
    
           
    
    

    
    