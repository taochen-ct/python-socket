import socket
import hashlib


host = ("127.0.0.1", 60000) # serve address

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp socket
thehash = hashlib.md5()  # hashlib

with open("crawl.ipynb", mode="rt", encoding="utf-8") as f:  # read file
    file = f.read()
    thehash.update(file.encode("utf-8"))
    file_hash = thehash.hexdigest()

client.sendto(str(len(file.encode("utf-8"))).encode("utf-8"), host)
client.sendto(file.encode("utf-8"), host)
data, addr = client.recvfrom(1024)
if data.decode("utf-8") == str(file_hash):
    print(f"{addr[0]}:{addr[1]}: OK")

client.close()
