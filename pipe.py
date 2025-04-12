from multiprocessing import Pipe, Process
import time

def filho(conn):
    print('Começando a receber mensagem...')
    msg = conn.recv()
    while msg != "FIM":
        print(f'Mensagem recebida: {msg}')
        msg = conn.recv()

if __name__ == "__main__":
    conn1, conn2 = Pipe(duplex=True)
    p = Process(target=filho, args=(conn1,))
    p.start()

    for i in range(10):
        msg = 'SO ' + str(i)
        conn2.send(msg)
        time.sleep(1)
    print('Processo pai terminado')
    conn2.send("FIM")
    
