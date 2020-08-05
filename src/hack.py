from win_memory_manager import MemoryManager
from addresses import STATUS, COINS, STATUS_LITTLE
from addresses import STATUS_NORMAL, STATUS_CAPE, STATUS_FLOWER


class Hack:
    """
    doc
    """
    def __init__(self, process_name):
        self.memory_manager = MemoryManager(process_name)

    def status_fixed(self):
        """
        Faz com que o status do Mário seja sempre o de com a capa
        """
        actual_state = self.memory_manager.read_byte(STATUS)
        print("Status atual: ", actual_state)
        if (actual_state != STATUS_CAPE):
            self.memory_manager.write_byte(
                STATUS,
                STATUS_CAPE.to_bytes(1, byteorder='little')
            )

    def have_99_coins(self):
        """
        Mantém o contador de moedas em 99, para que toda moeda coletada
        vire uma vida no decorrer do jogo
        """
        default_value = 99
        actual_value = self.memory_manager.read_byte(COINS)
        if actual_value != default_value:
            self.memory_manager.write_byte(
                COINS,
                default_value.to_bytes(1, byteorder='little')
            )
