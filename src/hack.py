from win_memory_manager import MemoryManager
from addresses import STATUS, COINS, STATUS_LITTLE
from addresses import STATUS_NORMAL, STATUS_CAPE, STATUS_FLOWER


class Hack:
    def __init__(self, process_name):
        self.memory_manager = MemoryManager(process_name)

    def status_fixed(self):
        """
        Mantém o status do mário sempre em 2, fazendo assim com que
        ele nunca perca a capa, e torne-se invencível
        """
        actual_state = self.memory_manager.read_byte(STATUS)
        print("Status atual: ", actual_state)
        if (actual_state != STATUS_CAPE):
            self.memory_manager.write_byte(
                STATUS,
                STATUS_CAPE.to_bytes(1, byteorder='little')
            )
            # O byteorder='little' significa 'little endian', é relacionado
            # ao modelo da arquitetura do processador.

    def have_99_coins(self):
        """
        Mantém o contador de moedas em 99, para que toda moeda coletada
        no decorrer do jogo vire uma vida
        """
        default_value = 99
        actual_value = self.memory_manager.read_byte(COINS)
        if actual_value != default_value:
            self.memory_manager.write_byte(
                COINS,
                default_value.to_bytes(1, byteorder='little')
            )
