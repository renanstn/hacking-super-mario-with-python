from ctypes import windll, sizeof
from ctypes.wintypes import ctypes
import psutil


PROCESS_ALL_ACCESS = 0x001F0FFF

class MemoryManager:
    """
    Classe que, através das funções providas pelo ctypes, lê e escreve
    valores diretamente na memória de outro processo sendo executado.
    """

    process_manager = None

    def __init__(self, process_name):
        """
        Procura o processo na lista de processos sendo executados no windows
        """
        for process in psutil.process_iter(['name', 'pid']):
            if process.info['name'] == process_name:
                self.process_id = process.info['pid']
                print("Processo encontrado. Iniciando coleta de dados...")
                print(self.process_id)
                self.attach_to_process()

    def attach_to_process(self):
        self.open_process = windll.kernel32.OpenProcess
        self.read_process_memory = windll.kernel32.ReadProcessMemory
        self.write_process_memory = windll.kernel32.WriteProcessMemory
        self.close_manager = windll.kernel32.CloseHandle
        self.process_manager = self.open_process(
            PROCESS_ALL_ACCESS, False, self.process_id
        )

    def read_byte(self, address):
        """
        Lê o valor armazenado em um endereço de memória
        """
        if self.process_manager == None:
            print("Gerenciador de processo não foi inicializado, abortando código")
            exit(1)

        # No caso do SNES, as variáveis que estamos trabalhando possuem
        # 1 byte de tamanho cada, por isso definimos o buffer logo abaixo
        # como um 'c_ubyte'. Para mais informações, segue o link:
        # https://docs.python.org/3/library/ctypes.html#fundamental-data-types
        buffer = ctypes.c_ubyte()
        bytread = ctypes.c_ubyte()

        self.read_process_memory(
            self.process_manager,
            address,
            ctypes.byref(buffer),
            ctypes.sizeof(buffer),
            ctypes.byref(bytread)
        )

        return buffer.value

    def write_byte(self, address, value):
        """
        Escreve um valor em um determinado endereço na memória
        """
        if self.process_manager == None:
            print("Gerenciador de processo não foi inicializado, abortando código")
            exit(1)

        buffer = ctypes.c_ubyte()
        bytread = ctypes.c_ubyte()

        self.write_process_memory(
            self.process_manager,
            address,
            value,
            ctypes.sizeof(buffer),
            ctypes.byref(bytread)
        )
