# coding:utf-8
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/12 17:07   tao.chen     1.0         No
"""

import socketserver
import json
import settings
from logger import logger
from Server.functions import execute_command


class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        while True:
            try:
                cmd = self.request.recv(1024).decode('gbk')
            except:
                break
            if not cmd:
                break

            terminal = execute_command(cmd, self.client_address)
            execute_result = terminal.execute()

            header = json.dumps({
                "client_address": self.client_address,
                "result_size": len(execute_result),
            })
            header_length = bytes(str(len(header)), "gbk").zfill(4)

            self.request.send(header_length)
            self.request.send(header.encode('gbk'))
            self.request.send(execute_result)

        self.request.close()


class myThreadingTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True


def start_server(server_adder=(settings.SERVER_HOST, settings.SERVER_PORT)):
    try:
        sk = myThreadingTCPServer(server_adder, RequestHandler)
        sk.serve_forever()
    except Exception as e:
        logger.critical(f"{e}")
