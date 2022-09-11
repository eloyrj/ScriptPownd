import sys
import requests
from stem import Signal
from stem.control import Controller


ruta = sys.argv[1] # Obtencio de la ruta del archivo desde *args


def newSesion():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    print("Peticion con ip con tor: ", session.get("https://ifconfig.me").text) #Impresion de la ip desde tor
    return session


def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='eloytor')
        controller.signal(Signal.NEWNYM)
        print("New Tor connection processed")
        controller.close()


print("Peticion con ip sin tor: ", requests.get("https://ifconfig.me").text) #Imprimimos la ip sin tor 


renew_connection()
session = newSesion() #conexion con tor 


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

f2 = open(ruta, "r", encoding='utf-8') #obtencion de los emails del archivo pasado por *args
lines = f2.readlines()
for email in lines:

    post = session.post(url="https://es.infobyip.com/verifyemailaccount.php", data={"email": email}, headers=headers) #Envio de la peticion al servidor 
    if (post.status_code == 403):
        print("Error 403: Reintentando conexion") #El servidor rechazo la conexion 
    else:

        if 0 <= post.text.find("is a valid email address"):
            print(email) # El email valido se imprime.
