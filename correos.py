
import argparse
import smtplib
import dns.resolver



def get_mx(hostname):
    try:
        servidor_mx = dns.resolver.resolve(hostname, 'MX')
    except:
        servidor_mx = None
        
    return servidor_mx

debug = True

def Validador(email):
    hostname = email[email.find("@") + 1:]
    s = get_mx(hostname)

    if s == None:
        print('No se encuentra MX para el dominio {}'.format(hostname))
        return None
    for mx in s:
        servidor = smtplib.SMTP(timeout=10)
        servidor.connect(str(mx.exchange))
        status, _ = servidor.helo()
        
        if status != 250:
            servidor.quit()
            continue
        servidor.mail('')
        status, _ = servidor.rcpt(email)
        if status == 250:
            servidor.quit()
            return True
            
        servidor.quit()
        
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""DESCRIPCIÓN: Este script comprueba si una dirección de correo existe en un MX (intercambiador de correo).""")
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument('-e', required=False, default=None,  help='Dirección de email a comprobar.')
    grupo.add_argument('-f', required=False, default=None,  help='Pasar la Ruta de un archivo en el que se alojan correos.')
    parser.add_argument('-s', required=False, default=None,  help='Ruta de un archivo en el que se imprimiran los correos validos.')
    argumentos = parser.parse_args()

    
    if (argumentos.e != None ):
        v = Validador(argumentos.e)
        if v:
            print("El correo {} es valido".format(argumentos.e))
        else:
            print("El correo {} no es valido".format(argumentos.e))
    elif(argumentos.f != None):
        f2 = open(argumentos.f, "r", encoding='utf-8') #obtencion de los emails del archivo pasado por *args
        lines = f2.readlines()
        if(argumentos.s!= None):
                salida = open(argumentos.s,"w",encoding="utf-8")
                
        for email in lines:
            
            v = Validador(email[:len(email)-1])
            if(argumentos.s!= None):
                if v:
                    salida.write(email)
            else:
                if v:
                    print(email[:len(email)-1])
                
        if(argumentos.s!= None):
                salida.close()
    
                