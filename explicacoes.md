Estudos gerais de Python desde o início

1 Operadores:
    Soma +
    Subtração -
    Divisão / (Sempre retorna valor real Float)
    Divisão // (Sempre retorna valores inteiros Int)
    Resto Divisão %
    Multiplicação *
    Potência **
    Prioridade ()
    Atribuição de valor =
    Menor <
    Menor igual <=
    Maior >
    Maior igual >=
    Igual ==
    Diferente !=

    -- Ordem de Precedência
    ()
    **
    *,/,//,%
    +,-

2 Variáveis
    Int (2,3,4 e etc).
    Float (4,3; 5,5; 9,8 e etc).
    Listas [tamanho];

3 Funções e métodos 
    print() função de saída de dados.
    lista.append() método que adiciona itens no final da lista
    len(lista) retorna o tamanho da lista
    range() função que gera progressões aritméticas
    input() função de entrada de valores

4 Estruturas
    4.1 Condicionais: 
    if condição:
        //Bloco de códigos
    elif condição:
        //Bloco de códigos
    else:
        //Bloco de códigos
   
    4.2 Repetições:
    for variavel in lista
        //Bloco de códigos
    while condição:
        //Bloco de códigos

5 Comandos
    break serve para interromper um laço de repetição, seja um for ou while.
    pass não faz nada, pode ser usada quando a sintaxe exige um comando mas a semântica não requer nenhuma ação.
    def inicia a definição de uma função, seguida pelo nome da função e sua lista de parâmetros.
    result retorna o valor de uma função

Notas Importantes
    Suporte nativo a números complexos usando j ou J para indicar a parte imaginária (3+5J).
    Para trabalhar com Strings podemos usar '' ou "" que teremos o mesmo resultado.
    Strings podem ser concatenadas com o operador + e repetidas com *.
    Não é utilizado chaves ou seja identação é tudo
    O comando for faz as iterações sobre os itens de qualquer sequência (Lista ou String) na sequência que aparecer.

    Tipos primitivos
        int: é o tipo de variável que recebe números inteiros
        float: é o tipo de variável que recebe números reais
        bool: é o tipo de variável que recebe somente os valores verdadeiro (True) e falso (False)
        str: tipo de variável que recebe textos

Manipulação de Strings 

len() - Retorna o tamanho de uma string - teste = 'Apostila de Python' len(teste)

capitalize() - Retorna a string com a primeira letra maiúscula - teste = 'python' a.capitalize()

count() - Informa quantas vezes um caracter ou sequência aparecem em uma string - b = 'Linguagem Python' b.count(b)

startswith() - Verifica se uma string começa com determinada sequência - c = 'Python' c.startswith('Py')