import socket
from datetime import datetime
import threading 

i = 0


def scan_port(target_ip, port):
    global i
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Porta {port} está aberta!")
            i += 1
        sock.close

    except KeyboardInterrupt:
        print("processo interrompido")
        exit()

    except socket.gaierror:
        print("\nHostname não pode ser resolvido")
        exit()

    except socket.error:
        print("\nErro ao conectar ao servidor")
        exit()

def start_scan(target_ip, port_range):
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
tempoI = start_time.strftime('%H : %M : %S')
print(f"Horario de inicio: {tempoI}")
print("-" * 50)

start_scan(target_ip, range(1, 1025))

if i == 0: 
    print("Nenhuma porta esta aberta!")

end_time = datetime.now()
tempoF = end_time.strftime('%H : %M : %S')
print("-" * 50)
print(f"Horario final: {tempoF}")
print(f"Tempo gasto no escaneamento: {(end_time - start_time)}")