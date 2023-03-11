# coding:utf-8
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/12 17:07   tao.chen     1.0         No
"""
import subprocess
from logger import logger

def get_log(func):
    def handle_log(*args, **kwargs):
        client = args[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"{client.addr[0]}:{client.addr[1]} {e}")
    return handle_log

class functions:
    """static functions"""

    @staticmethod
    def split_command(command):
        splited_command = command.split(" ")
        if splited_command[0] not in FUNCTION.keys():
            return functions.execute_terminal_command
        return FUNCTION[splited_command[0]]

    @staticmethod
    def execute_terminal_command(cmd):
        terminal = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        execute_result = terminal.stdout.read()
        return execute_result

    @staticmethod
    def transmit_file(cmd):
        file_path = cmd.split(" ")[1]
        with open(file_path, mode="rb") as f:
          file = f.read()
        return file


class execute_command(functions):
    """Execute a command"""

    def __init__(self, cmd, *args, **kwargs):
        self.cmd = cmd
        self.addr = args[0]

    @get_log
    def execute(self):
        func = self.split_command(self.cmd)
        result = func(self.cmd)

        logger.info(f"CLIENT:{self.addr[0]}:{self.addr[0]} {self.cmd}")
        return result


FUNCTION = {
    "get": functions.transmit_file,
}
