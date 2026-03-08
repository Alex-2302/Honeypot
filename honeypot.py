import socket
import logging
from datetime import datetime

HOST = "0.0.0.0"
PORT = 2222

logging.basicConfig(filename="logs.txt", level=logging.INFO)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("SSH Honeypot running on port 2222...")

while True:
    client, addr = server.accept()
    
    attacker_ip = addr[0]
    print(f"Connection from {attacker_ip}")

    logging.info(f"{datetime.now()} - Connection from {attacker_ip}")

    client.send(b"SSH-2.0-OpenSSH_7.4\n")

    data = client.recv(1024)

    logging.info(f"{datetime.now()} - Data received: {data}")

    client.close()
