import socket
from datetime import datetime

target = input("Digite o IP ou dominio que voce quer escanear: ")

target_ip = socket.gethostbyname(target)


print(f"Escaneando {target_ip}")
print("-" * 50)
start_time = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Porta {port} esta aberta!")
        sock.close()

except KeyboardInterrupt:
    print("processo interrompido")
    exit()

except socket.gaierror:
    print("\nHostname não pode ser resolvido")
    exit()

except socket.error:
    print("\nErro ao conectar ao servidor")
    exit()

end_time = datetime.now()
print(f"Tempo gasto no escaneamento: {end_time - start_time}")