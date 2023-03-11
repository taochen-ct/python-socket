import socket
import hashlib


serve = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # tcp/udp
serve.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置端口复用
serve.bind(("127.0.0.1", 60000))  # 绑定ip+端口

thehash = hashlib.md5()

while True:
    data, addr = serve.recvfrom(1024)
    file_data, addr = serve.recvfrom(int(data.decode("utf-8")))
    thehash.update(file_data)
    file_hash = thehash.hexdigest()
    print(file_hash)
    serve.sendto(str(file_hash).encode('utf-8'), addr)
    file = file_data.decode('utf-8')
    with open("file.ipynb", mode="wt", encoding="utf-8") as f:
        f.write(file)