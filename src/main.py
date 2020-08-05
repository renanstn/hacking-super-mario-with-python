from hack import Hack
from time import sleep


process_name = "snes9x-x64.exe"

hack_mario = Hack(process_name)

while True:
    hack_mario.status_fixed()
    hack_mario.have_99_coins()
    sleep(0.5)
