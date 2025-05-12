import process
import round_robin
from multiprocessing import Process

if __name__ == "__main__":

    processo = process.Process()
    fila = []
    

    p1 = Process(target=processo.func1)
    p2 = Process(target=processo.func2, args=(1,))
    p3 = Process(target=processo.func3, args=(1,))

    fila.append(p1)
    fila.append(p2)
    fila.append(p3)

    rr = round_robin.Round_Robin(fila, 2)
    rr.executar()