import os
from threading import Thread
from multiprocessing import Process, Pipe, Value

# Função para usar com Threads
def f(c):
    global a
    a = a + 1
    c = c + 1
    print(os.getpid())

# Função para usar com Processos
def f1(d, e):
    d.send("oi")
    print(os.getpid())
    e.value = e.value + 1

a = 1

if __name__ == "__main__":
    b = 1
    
    # Usando Thread
    t = Thread(target=f, args=(b,))
    t.start()
    t.join()
    print(a, b)
    
    # Usando Process
    t = Process(target=f, args=(b,))
    t.start()
    t.join()
    print(a, b)

    print(os.getpid())
    
    # Criando Pipe e Value
    c, d = Pipe()
    e = Value('i', 1)

    # Usando Process com Pipe e Value
    t = Process(target=f1, args=(c, e))
    t.start()
    print(d.recv())
    t.join()
    
    print(a, b, e.value)
