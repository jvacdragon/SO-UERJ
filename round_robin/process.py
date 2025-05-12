import os
import time
import signal

class Process():
    def __init__(self):
        self.valor_func2 = 0
        self.func2_executada = False
        self.inicio_func2 = None
        self.tempo_func2_executado = 0
        signal.signal(signal.SIGCONT, self.continuar_func2)

    def func1(self):
        print(f'Iniciando processo que tem tempo de 4 segundos e pid de: {os.getpid()}')
        with open("log.txt", "a") as arquivo:
            arquivo.write(f"Iniciando processo que tem tempo de 4 segundos e pid de: {os.getpid()}\n")

        time.sleep(4)

        print(f'Finalizando processo: {os.getpid()}')
        with open("log.txt", "a") as arquivo:
            arquivo.write(f"Finalizando processo: {os.getpid()}\n")

    def func2(self, tempo_execucao):
        print(f'Inicio da função, com pid = {os.getpid()}, que vai ter um looping que soma de 1 em 1 no tempo definido: {tempo_execucao} segundos')
        with open("log.txt", "a") as arquivo:
            arquivo.write(f"Inicio da função, com pid = {os.getpid()}, que vai ter um looping que soma de 1 em 1 no tempo definido: {tempo_execucao} segundos\n")
        
        self.func2_executada = True
        self.inicio_func2 = time.time()

        while self.tempo_func2_executado < tempo_execucao:
            self.valor_func2 += 1
            agora = time.time()
            self.tempo_func2_executado += agora - self.inicio_func2
            self.inicio_func2 = agora

        print(f'Termino do processo com pid de {os.getpid()} e valor final sendo: {self.valor_func2}')
        with open("log.txt", "a") as arquivo:
            arquivo.write(f"Termino do processo com pid de {os.getpid()} e valor final sendo: {self.valor_func2}\n")

    def func3(self, n):
        print(f"Inicio da funcao de fibonacci por segundo com pid = {os.getpid()}")
        with open("log.txt", "a") as arquivo:
            arquivo.write(f"Inicio da funcao de fibonacci por segundo com pid = {os.getpid()}\n")

        if n <= 1:
            print(f"Fim da funcao de fibonacci com pid = {os.getpid()}, valor final: {n}")
            with open("log.txt", "a") as arquivo:
                arquivo.write(f"Fim da funcao de fibonacci com pid = {os.getpid()}, valor final: {n}\n")

            return

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            print(f"Fibonacci atual: {b}")
            with open("log.txt", "a") as arquivo:
                arquivo.write(f"Fibonacci atual: {b}\n")

            time.sleep(1)
        print(f"Fim da funcao de fibonacci com pid = {os.getpid()}, valor final: {b}")
        with open("log.txt", "a") as arquivo:
                arquivo.write(f"Fim da funcao de fibonacci com pid = {os.getpid()}, valor final: {b}\n")

    def continuar_func2(self, sigmum, frame):
        if self.func2_executada:
            self.inicio_func2 = time.time()
