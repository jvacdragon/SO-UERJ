from multiprocessing import Process, Queue
import time

fila = Queue(3)

def filho(fila: Queue):
    while True:
        val = fila.get() #metodo get() espera até que tenha uma valor na fila para que seja executado
        if val=="FIM":
            print("Fim do processo filho")
            break
        print(f'o valor é: {val}')
        time.sleep(2)

if __name__ == '__main__':
    p = Process(target=filho, args=(fila,))
    p.start()

    for i in range(0,10):
        fila.put(i)
        time.sleep(1)
        
    fila.put("FIM")
    p.join()
    print('processo pai encerrado')