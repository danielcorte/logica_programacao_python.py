from time import sleep
import os

sistema = os.name

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class Semafaro:
    def __init__(self, verde=False, amarelo=False, vermelho=True):
        self.verde = verde
        self.amarelo = amarelo
        self.vermelho = vermelho

    def sinalVerde(self):
            sleep(6)
            self.vermelho = False
            self.verde = True
            print(f"--------------------\n      semafaro\n--------------------\n[{GREEN}O{RESET}] - Verde\n[ ] - Amarelo\n[ ] - Vermelho\n--------------------")
            self.sinalAmarelo()

    def sinalAmarelo(self):
            sleep(6)
            self.verde = False
            self.amarelo = True
            print(f"--------------------\n      semafaro\n--------------------\n[ ] - Verde\n[{YELLOW}O{RESET}] - Amarelo\n[ ] - Vermelho\n--------------------")
            self.sinalVermelho()

    def sinalVermelho(self):
            sleep(2)
            self.amarelo = False
            self.vermelho = True
            print(f"--------------------\n      semafaro\n--------------------\n[ ] - Verde\n[ ] - Amarelo\n[{RED}O{RESET}] - Vermelho\n--------------------")
            self.sinalVerde()


trafego = Semafaro()

while True:
    trafego.sinalVerde()
