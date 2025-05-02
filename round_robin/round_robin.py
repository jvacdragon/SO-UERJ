import os
import signal
import time

class Round_Robin():

    def __init__(self, fila_processos, quantum_segundos):
        self.fila_processos = fila_processos
        self.quantum_segundos = quantum_segundos

    def executar(self):

        while(len(self.fila_processos) > 0):
            processo_atual = self.fila_processos.pop(0)

            if(not processo_atual.is_alive()):
                processo_atual.start()

            os.kill(processo_atual.pid, signal.SIGCONT)

            time.sleep(self.quantum_segundos)

            os.kill(processo_atual.pid, signal.SIGSTOP)
            if(processo_atual.is_alive()):
                self.fila_processos.append(processo_atual)

        print("fim do round robin")

    def get_fila_processos(self):
        return self.fila_processos