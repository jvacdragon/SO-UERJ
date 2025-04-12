import os
import time
from multiprocessing import Process


def processoFilho():
    print(f'Iniciando processo filho: {os.getpid()}')
    time.sleep(3)
    print(f'Finalizando processo filho: {os.getpid()}')
    
if __name__ == '__main__': #aqui está identificando o arquivo principal aonde está rodando o processo. Caso a função esteja sendo importada de outro arquivo .py e isso nao seja utilizado, é possivel ocorrer um looping.
    print(f'iniciando processo pai: {os.getpid()}')
        
    p = Process(target=processoFilho)
    p.start()
        
    time.sleep(3)
        
    #p.join() #para que o processo filho termine antes do processo pai continuar após o join()
    
    print(f'Finalizando processo pai: {os.getpid()}')
        
"""
CÓDIGO NO LINUX SERIA ASSIM:

import os
import time
from multiprocessing import Process


pid = os.fork()

if pid == 0:
    print(f'Iniciando processo filho: {os.getpid()}')
    time.sleep(3)
    print(f'Finalizando processo filho: {os.getpid()}')
    
else:
    print(f'Iniciando processo pai: {os.getpid()}')
    time.sleep(3)
    print(f'Finalizando processo pai: {os.getpid()}') """