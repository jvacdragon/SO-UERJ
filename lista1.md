1. Sobre processos e threads:

* Qual a diferença entre fork ou Process?

A diferença é que em Process se é criado um novo processo, enquanto em fork o processo principal é duplicado em outro processo.

* Qual a diferença entre um processo e uma thread?

A thread é uma subdivisão de um processo, de forma que, diversas threads dentro de um processo podem acessar o mesmo pedaço de memória, pois esse pedaço de memória é exclusivo do processo todo e nao de uma thread. Enquanto um processo não pode compartilhar espaços de memória com outros processos, de forma que, até seus ID são diferentes.

* Dê 1 exemplo de aplicação que se beneficia do paralelismo e 1 exemplo que nao pode ser paralelizada:

Exemplo de paralelismo: Renderizaçao gráfica, pois cada parte da renderização pode ser renderizada por uma thread diferente e processada simultaneamente

Exemplo de não paralelismo: Processamentos que utilizam de programação recursiva, como o cálculo de Fibonacci recursivo, onde para ter o dado que se deseja, se tem dependência de dados anteriores.

2. Sobre o código a seguir

```python
import os
from threading import Thread
from multiprocessing import Process, Pipe, Value

#Função para usar com Threads
def f(c):
    global a
    a= a+1
    c=c+1
    print(os.getpid())

#Função para usar com Processos
def f1(d,e):
    d.send("oi")
    print(os.getpid())
    e.value=e.value+1
a=1

if __name__ = "__main__":
    b = 1

    #Usando Thread
    t=Thread(target=f, args=(b,))
    t.start()
    t.join()
    print(a,b)

    #Usando Process
    t = Process(target=f, args=(b,))
    t.start()
    t.join()
    print(a,b)

    print(os.getpid())

    #Ciando Pipe e Value
    c, d = Pipe()
    e=Value('i',1)

    #usando Process com Pipe e Value
    t = Process(target=f1,args=(c,e))
    t.start()
    print(d.recv)
    t.join()
    print(a,b,e.value)
```

* Marque quais linhas ocorrem chamadas de sistema e justifique sua resposta:

Todas as linhas com os.getpid(), pois chamam o módigo do SO para identificação dos processos. A linhas com t = Thread() e t.join(), pois a criação de threads sao feitas com auxilio do sistema operacional. As linhas com t.start() também, pois o SO que inicializa o processo. As linhas com Pipe() ja que cria uma comunicação entre processos que só pode ser fetia com permissão do SO e em seguia Value() que cria uma memória compartilhada entre os processos, o que exige permissao do SO também.

* Diga o que o código imprime, assumindo que o PID do processo pai seja 3020 e que o pid dos filhos sejam criados sequencialmente.

print 1: 3020
print 2: 2,1
print 3: 3021
print 4: 2,1
print 5: 3020
print 6: 3022
print 7: "oi"
print 8: 2,1,2

3. Explique e dê um exemplo de como funciona o escalonamento de processos, a troca de contexto, o funcionamento das interrupções e o tratamento de entrada e saída dem um sistema preemptivo:

Escalonamento de processos é o gerenciamento dos processos do SO, está relacionado a definição de prioridade dos processos que devem ocorrer antes dos outros, consumindo assim recursos como memória e CPU. Um exemplo pode ser ao ligar o computador, quando o computador decide os processos principais que devem ser inicializados antes de quaisquer outros por conta de prioridade, como carregamento do SO, antivirus e outros programas.

A troca de contexto ocorre quando se está utilizando um programa e então se é trocado para outro programa. Ao trocar do programa 1 para o programa 2, os dados do programa 1 sao salvados na memória para que quando se volte para o programa 1, ele se inicie do ponto onde estava anteriormente. Um exemplo seria ao trocar de janelas do navegador.

As interrupções servem para quando ocorre algum erro no fluxo do processo de um programa e então elas ocorrem para que o sistema nao quebre. Interrupções podem acontecer de forma a terem ou nao tratamento. Um exemplo seria um código com blocos try-catch para tratamento de erro. O processo ocorre no bloco try e caso ocorra algum erro, ele deve ser tratado no bloco catch

O tratamento de entrada e saída em um sistema preemptivo, como ler um disco ou esperar uma resposta da rede, fazem com que o sistema deva esperar. Enquanto está no estado de espera, o escalonador de processos é acionado e define outro processo para rodar enquanto esse processo I/O está em espera.

4. Explique o que é:

* Kernel:

É o núcleo do sistema operacional, responsavel onde se é possível executar ações que normalmente nao sao possíveis no modo usuário, como gerenciar diretamente a memória do computador e também é o que gerencia os recursos do sistema(CPU, memória, etc)

* BIOS

Responsável pela inicialização do computador e gerenciamento do flluxo de dados entre os dispositivos de entrada e saída  e o sistema operacional.

* Hierarquia de memória

Hierarquia das memórias de um computador, quando maior a memória e mais rápida, maior é o custo dela. Exemplos de memórias sao cache, HD, SSD.

5.	Cite e explique 3 funções do sistema operacional:

Gerenciamento dos recursos do computador, como CPU e memória
Interface gráfica para facilitar o uso do computador
Facilidade no gerenciamento de pastas e arquivos