# Simulador ede escalonador Round-Robin
Aplicação que visa simular um escalonador Round-Robin utilizando estrutura de classe para o escalonador e para os processos.

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação. Aqui o usuário define quais funções de `process.py` serão executadas, com quais argumentos, e monta a fila de processos para ser executada pelo escalonador.
- `process.py`: Contém a classe `Process`, com três funções que simulam tarefas computacionais.
- `round_robin.py`: Implementa o algoritmo de escalonamento Round Robin.
- `log.txt`: Arquivo de log criado e sobrescrito automaticamente a cada execução, contendo o registro detalhado de cada processo.

---

## process.py

A classe Process, que está no arquivo process.py, tem 5 métodos, sendo eles:

- \__init__ -> Inicializa a classe e as variáveis de controle para o método func2. Também contém o comando para que sempre que um SIGCONT seja utilizado, a classe utilize o método continuar_func2

- func1 -> Método que está determinado para acontecer sempre por 4 segundos

- func2 -> Método que recebe um número como parâmetro para determinar seu tempo de execução em segundos. Ele começa uma contagem em um looping que termina ao fim do tempo passado como parâmetro

- func3 -> Método que recebe um valor n que irá determinar quantos segundos deve durar a execução. TAmbém representa até aonde irá calcular o valor da sequência de Fibonacci. Exemplo: se n for igual a 5, então o resultado final será o quinto número da sequência de Fibonacci

- continuar_func2 -> Método que serve para auxiliar func2. Sempre que for utilizado um SIGCONT no processo que estiver rodando func2, essa função será acionada para que func2 volte a executar a partir do mesmo tempo de antes, para que não haja perda de segundo entre um SIGSTOP e o SIGCONT usado em func2.

## round_robin.py
Classe responsável pelo escalonamento do Round-Robin. Contém os métodos:

- \__init__ -> Responsável pela inicialização do escalonador. Recebe como parâmetros uma lista com os processos a serem executados e um tempo quantum em segundos para determinar o tempo que cada processo será executado antes de pausar.

- executar -> Onde os processos são executados utilizando o escalonador

- get_fila_processos -> retorna a fila de processos atual do escalonador

## Como Executar

No arquivo main.py, já foi deixado um exemplo de como utilizar a aplicação:

```python
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

```

A ideia é criar processos com o objeto processo junto do módulo Process, então sempre que quiser criar um processo, se deve seguir a seguinte estrutura:

- NOME-DA-VARIAVEL = Process(target=processo.MÉTODO-DA-CLASSE-PROCESSO)

Após isso se dede adicionar todos os processos criados para o lista com o nome de fila, no exemplo do código essa adição foi feita utilizando fila.append(NOME-DA-VARIAVEL)

Por fim se deve criar a classe round-robin e executa-la da seguinte forma:

- NOME-DA-VARIAVEL-ROUND-ROBIN = round_robin.Round_Robin(fila, QUANTUM-EM-SEGUNDOS-DESEJADO)
- NOME-DA-VARIAVEL-ROUND-ROBIN.executar()
