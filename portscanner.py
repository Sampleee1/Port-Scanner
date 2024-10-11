import socket
from datetime import datetime
import threading 
import time

i = 0

def grab_banner(sock):
    try:
        sock.send(b'HEAD / HTTP/ 1.1\r\n\r\n')
        banner = sock.recv(1024).decode('utf-8')
        return banner.decode().strip()
        return IdeServ(banner)

    except Exception as e:
        return f"Erro ao capturar o banner: {str(e)}"
    

def IdeServ(banner):
    common_services = {
        "Apache": "apache",
        "Nginx": "nginx",
        "SSH": "ssh",
    	"FTP": "ftp",
        "MySQL": "mysql",
        "SMTP": "smtp",
        "Telnet": "telnet",
        "Microsoft IIS": "Microsoft-IIS"
    }

    for service, palavra_chave in common_services.items():
        if palavra_chave.lower() in banner.lower():
            return f"Serviço detectado: {service}"
        
    return f"Serviço não identificado no banner."


def scan_port(target_ip, port):
    global i
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Porta {port} está aberta!")
            banner = grab_banner(sock)
            print(f"Banner da porta {port}: {banner}")
            i += 1
        sock.close
        time.sleep(0.1)

    except KeyboardInterrupt:
        print("processo interrompido")
        exit()

    except socket.gaierror:
        print("\nHostname não pode ser resolvido")
        exit()

    except socket.error:
        print("\nErro ao conectar ao servidor")
        exit()

def start_scan(target_ip): # Sistema de Threads
    threads = []

    for port in range(1, 1025):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


target = input("Digite o IP ou dominio que voce quer escanear: ")

target_ip = socket.gethostbyname(target)

print("\n" * 100)
print(f"Escaneando {target} ({target_ip})")
start_time = datetime.now()
tempoI = start_time.strftime('%H:%M:%S')
print(f"Horario de inicio: {tempoI}")
print("-" * 50)

start_scan(target_ip)

if i == 0: 
    print("Nenhuma porta esta aberta!")

end_time = datetime.now()
tempoF = end_time.strftime('%H : %M : %S')
print("-" * 50)
print(f"Horario final: {tempoF}")
print(f"Tempo gasto no escaneamento: {(end_time - start_time)}")