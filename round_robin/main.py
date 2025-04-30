import process
from multiprocessing import Process


if __name__ == "__main__":

    processo = process.Process()
    processo2 = process.Process()

    p1 = Process(target=processo.func1)
    p2 = Process(target=processo.func2, args=(2,))

    p1.start()
    p2.start()

    

