# Trabalho Individual 1 - Karatsuba - João Pedro Mairinque

## Algoritmo de Karatsuba

O algoritmo de Karatsuba é um método eficiente para a multiplicação de números grandes, reduzindo a complexidade da abordagem tradicional de O(n²) para O(n<sup>log₂(3)</sup>). Nesta atividade, analiso a complexidade ciclomática e assintótica da implementação do algoritmo em Python.

## Complexidade Ciclomática

A complexidade ciclomática (M) mede a complexidade do fluxo de controle do programa. Para calcular M, seguimos os seguintes passos:

## Fluxo de Controle da Função

### Nós

O fluxo de controle da função `karatsuba(x, y)` pode ser representado por um grafo de fluxo com as seguintes principais decisões:

- **Nó 1**: Início da função (`if x < 10 or y < 10`)
- **Nó 2**: Primeiro IF (se `x < 10` ou `y < 10`)
  **Nó 3**: Retorno do primeiro IF (`n = max(len(str(x)), len(str(y)))` e `m = n // 2`)
- **Nó 4**: Cálculo do tamanho do número `n = max(len(str(x)), len(str(y)))`
- **Nó 5**: Cálculo do tamanho do número `m = n // 2`
- **Nó 6**: Cálculo das partes altas e baixas iniciais (`x_high, x_low = divmod(x, 10**m)`)
- **Nó 7**: Cálculo das partes altas e baixas secundárias (`y_high, y_low = divmod(y, 10**m)`)
- **Nó 8**: Primeira chamada recursiva `a = karatsuba(x_high, y_high)`
- **Nó 9**: Segunda chamada recursiva `b = karatsuba(x_low, y_low)`
- **Nó 10**: Terceira chamada recursiva `c = karatsuba(x_high + x_low, y_high + y_low) - a - b`
- **Nó 11**: Retorno final `return a * 10**(2*m) + c * 10**m + b`

### Arestas

As arestas representam o fluxo entre os nós do grafo:

- **(1 → 2)**: Início da função ao primeiro IF
- **(2 → 3)**: Primeiro IF ao retorno se true
- **(2 → 4)**: Se false, segue para calcular `n`
- **(4 → 5)**: Do cálculo de `m` ao de `n`
- **(5 → 6)**: Calcula `x_high` e `x_low`
- **(6 → 7)**: Calcula `y_high` e `y_low`
- **(7 → 8)**: Chama `karatsuba(x_high, y_high)`
- **(8 → 9)**: Chama `karatsuba(x_low, y_low)`
- **(9 → 10)**: Chama `karatsuba(x_high + x_low, y_high + y_low) - a - b`
- **(10 → 11)**: Retorna o resultado final

Total de 10 arestas

## Cálculo da Complexidade Ciclomática

A fórmula para calcular a complexidade ciclomática é:

M = E - N + 2P

Onde:

- **E**: Número de arestas
- **N**: Número de nós
- **P**: Número de componentes conexos (para um programa simples, P = 1)

Ao analisar a função `karatsuba`, estimamos os seguintes valores:

- **N = 11** (decisões, chamadas recursivas e operações principais)
- **E = 10** (fluxo de controle entre as operações)
- **P = 1** (uma única função principal)

Assim, a complexidade ciclomática é:

M = 10 - 11 + 2*(1) = 2

A complexidade ciclomática significa que o programa possui dois caminhos lineares independentes de execução. Isso se deve ao fato de que a estrutura de controle inclui apenas uma condição de decisão (`if x < 10 or y < 10`), que determina se o programa segue para o cálculo normal da multiplicação ou entra no processo recursivo de Karatsuba.

Os dois caminhos possíveis são:

### Caminho 1 (Caso Base)

Se `x < 10` ou `y < 10`, o programa retorna diretamente `x * y`.

### Caminho 2 (Recursivo)

Se `x >= 10` e `y >= 10`, o algoritmo executa os seguintes passos:

1. Divide os números em partes altas e baixas.
2. Chama Karatsuba recursivamente três vezes.
3. Retorna o resultado da composição dos produtos parciais.

Assim, a função `karatsuba(x, y)` sempre seguirá um dos dois fluxos possíveis, garantindo que sua complexidade ciclomática seja exatamente **2**.

## Complexidade Assintótica

O algoritmo de Karatsuba reduz o número de multiplicações necessárias utilizando a estratégia de divisão e conquista. Sua complexidade é definida pela seguinte relação de recorrência:

T(n) = 3T(n/2) + O(n)

Usando o Teorema Mestre T(n) = aT(n/b) + O(n<sup>d</sup>), temos:

- a = 3 (três subproblemas gerados)
- b = 2 (o problema é dividido em duas partes)
- d = 1 (operações são O(n))

Θp = Θ(n<sup>log₂(3)</sup>)

Aproximadamente:

Θ(n<sup>1.585</sup>)

Como O(n) cresce mais lentamente que O(n<sup>p</sup>), Logo T(n) = Θ(n<sup>1.585</sup>)

### Melhor Caso

O melhor caso ocorre quando um dos números é pequeno o suficiente para acionar a condição base (x < 10 ou y < 10), resultando em uma multiplicação direta O(1).

### Caso Médio

No caso médio, os números têm tamanhos comparáveis, e o algoritmo executa recursivamente três multiplicações para cada divisão em duas partes, levando a O(n<sup>1.585</sup>).

### Pior Caso

O pior caso também segue O(n<sup>1.585</sup>), pois a estrutura recursiva sempre se mantém constante. No entanto, pode haver overhead adicional se os números não forem exatamente potências de 2.

## Execução



### Executando o projeto



Acesse a raiz do projeto no terminal e execute:

```bash
python3 main.py
```

### Caso não possua o python

### MacOS

Instale o python 3 com Homebrew

```bash
brew install python
```

### Windows

1. Baixe o instalador do Python no site oficial:  
   [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Durante a instalação, marque a opção **"Add Python to PATH"**.
3. Após a instalação, abra um novo terminal e confirme a instalação com:

```bash
python --version
```

## Documentação e links úteis

- [Algoritmo de Karatsuba](https://pt.wikipedia.org/wiki/Algoritmo_de_Karatsuba)
- [Karatsuba - IME](https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/karatsuba.html)

## Licença

Este projeto está licenciado sob a Licença MIT. e execute:
