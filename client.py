# coding:utf-8
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/12 17:07   tao.chen     1.0         No
"""
import socket
import json

# client
host = ('127.0.0.1', 60000)  # server address
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket class
sk.connect(host)  # estiablish connection

with sk:
    while True:
        cmd = input("entre command>>").strip()
        if cmd == "q": break
        if cmd == "": continue
        # senf terminal command
        sk.send(cmd.encode("utf-8"))
        # receive executed result header(data size)
        header_length = int(sk.recv(4).decode("utf-8"))
        header = json.loads(sk.recv(header_length).decode("utf-8"))

        received_result_size = 0
        result = b''
        while header["result_size"] > received_result_size:
            result += sk.recv(1024)
            received_result_size += len(result)

        print(f"server {host[0]}:{host[1]}\n", result.decode('utf-8'))
