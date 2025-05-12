import os
import signal
import time

class Round_Robin():

    def __init__(self, fila_processos, quantum_segundos):
        self.fila_processos = fila_processos
        self.quantum_segundos = quantum_segundos

        with open("log.txt", "w") as arquivo:
            arquivo.write("")

    def executar(self):

        while(len(self.fila_processos) > 0):
            processo_atual = self.fila_processos.pop(0)

            if(not processo_atual.is_alive()):
                processo_atual.start()

            os.kill(processo_atual.pid, signal.SIGCONT)

            time.sleep(self.quantum_segundos)

            if(processo_atual.is_alive()):
                os.kill(processo_atual.pid, signal.SIGSTOP)
                self.fila_processos.append(processo_atual)

        print("fim do round robin")
        with open("log.txt", "a") as arquivo:
            arquivo.write("fim do round robin\n")

    def get_fila_processos(self):
        return self.fila_processos