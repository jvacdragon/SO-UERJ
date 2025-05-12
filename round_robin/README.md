# Simulador ede escalonador Round-Robin
Aplicação que visa simular um escalonador Round-Robin utilizando estrutura de classe para o escalonador e para os processos.

## 📁 Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação. Aqui o usuário define quais funções de `process.py` serão executadas, com quais argumentos, e monta a fila de processos para ser executada pelo escalonador.
- `process.py`: Contém a classe `Process`, com três funções que simulam tarefas computacionais.
- `round_robin.py`: Implementa o algoritmo de escalonamento Round Robin.
- `log.txt`: Arquivo de log criado e sobrescrito automaticamente a cada execução, contendo o registro detalhado de cada processo.

---

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








