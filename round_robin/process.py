import os
import time
import signal

class Process():

    esta_rodando  = True
    valor_func2 = 0

    func2_executada = False
    inicio_func2 =  None
    tempo_func2_executado = 0
    func2_pausa_iniciada = None

    def __init__(self):
        signal.signal(signal.SIGCONT, self.continuar_func2)

    def func1(self):
        print(f'iniciando processo que tem tempo de 4 segundos e pid de: {os.getpid()}')
        time.sleep(4)
        print(f'finalizando processo: {os.getpid()}')
        self.set_esta__rodando(False)

    def func2(self, tempo_execucao):
        
        print(f'inicio da função que vai ter um looping que soma de 1 em 1 no tempo definido: {tempo_execucao} segundos')
        self.set_func2_executada(True)
        self.set_inicio_func2(time.time())
        
        while(self.get_tempo_func2_executado() < tempo_execucao):
            self.set_valor_func2(self.get_valor_func2() + 1)
            agora = time.time()
            self.set_tempo_func2_executado(self.get_tempo_func2_executado() + agora - self.get_inicio_func2())
            self.set_inicio_func2(agora)

        print(f'termino do processo com pid de {os.getpid()} e valor final sendo: {self.get_valor_func2()}')
        self.set_esta__rodando(False)

    def continuar_func2(self):
        if(self.get_func2_executada()):
            self.set_inicio_func2(time.time())

    def get_valor_func2(self):
        return self.valor_func2
    
    def get_esta_rodando(self):
        return self.esta_rodando
    
    def get_func2_executada(self):
        return self.func2_executada
    
    def get_inicio_func2(self):
        return self.inicio_func2
    
    def get_tempo_func2_executado(self):
        return self.tempo_func2_executado
    
    def get_func2_pausa_iniciada(self):
        return self.func2_pausa_iniciada
    
    def set_func2_pausa_iniciada(self, novo_valor):
        self.func2_pausa_iniciada = novo_valor
    
    def set_tempo_func2_executado(self, novo_valor):
        self.tempo_func2_executado = novo_valor
    
    def set_inicio_func2(self, novo_valor):
        self.inicio_func2 = novo_valor
    
    def set_func2_executada(self, novo_valor):
        self.func2_executada = novo_valor
    
    def set_esta__rodando(self, novo_valor):
        self.esta_rodando = novo_valor

    def set_valor_func2(self, novo_valor):
        self.valor_func2 = novo_valor
