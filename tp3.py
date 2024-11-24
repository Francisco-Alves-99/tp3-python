# EXERCÍCIO 1:
def retorna_quadrados(lista):
    """
    Recebe uma lista de números e retorna uma nova lista contendo os quadrados 
    de cada elemento da lista original.

    Parâmetros:
    lista (list): Uma lista de números (inteiros ou flutuantes).

    Retorna:
    list: Uma lista contendo os quadrados dos números da lista de entrada.
    
    Exemplo:
    >>> retorna_quadrados([1, 2, 3])
    [1, 4, 9]
    """

    quadrados = [x ** 2 for x in lista] # solução em apenas uma linha
    return quadrados

def recebe_lista():
    """
    Solicita ao usuário que insira números, adicionando-os a uma lista. 
    O processo continua até que o usuário escolha sair. Após a entrada dos números, 
    a função imprime os quadrados de cada número inserido, utilizando a função `retorna_quadrados`.

    A função não recebe parâmetros e não retorna valores. Ela interage com o usuário por meio de 
    entradas de texto e exibe o resultado diretamente.

    Exemplo de execução:
    Digite um número para adicionar a lista: 4
    Digite 1 para adicionar outro número ou 2 para sair: 1
    Digite um número para adicionar a lista: 5
    Digite 1 para adicionar outro número ou 2 para sair: 2
    Resultado: [16, 25]
    
    Observação:
    A função depende da função `retorna_quadrados` para calcular e exibir os quadrados dos números inseridos.
    """
    lista = []
    while True:
        numero = int(input("Digite um número para adicionar a lista: "))
        lista.append(numero)
        escolha = int(input("Digite 1 para adicionar outro número ou 2 para sair "))
        if (escolha == 2):
            break
    print(retorna_quadrados(lista))

recebe_lista()

# EXERCÍCIO 2:
def verifica_numeros(lista):
    """
    Recebe uma lista de números e retorna uma nova lista onde todos os números 
    menores que 10 são substituídos por 0, e os demais números permanecem inalterados.

    Parâmetros:
    lista (list): Uma lista de números (inteiros ou flutuantes).

    Retorna:
    list: Uma nova lista com os números modificados conforme a condição:
          - Números menores que 10 são substituídos por 0.
          - Números maiores ou iguais a 10 permanecem os mesmos.
    
    Exemplo:
    >>> verifica_numeros([3, 12, 5, 15, 8])
    [0, 12, 0, 15, 0]
    """

    nova_lista = [0 if x < 10 else x for x in lista] # solução em apenas uma linha
    return nova_lista

print(verifica_numeros([1,2,3,4,25]))

# EXERCÍCIO 3:
def conta_palavras(lista):
    """
    Conta o número de palavras em cada string de uma lista.

    A função recebe uma lista de strings e retorna uma lista contendo o número de palavras em cada string. 
    Cada palavra é considerada como uma sequência de caracteres separada por espaços em branco.

    Parâmetros:
    lista (list of str): Uma lista de strings, onde cada string pode conter uma ou mais palavras.

    Retorna:
    list of int: Uma lista de inteiros representando o número de palavras em cada string da lista de entrada.

    Exemplo:
    >>> conta_palavras(["Olá mundo", "Python é incrível", "Teste"])
    [2, 3, 1]
    """

    num_de_palavras = [len(x.split()) for x in lista] # solução em apenas uma linha
    return num_de_palavras

def recebe_historia():
    """
    Recebe uma série de frases do usuário e imprime o número de palavras em cada frase.

    A função solicita ao usuário que insira frases, uma por vez, e continua a pedir novas frases até que o usuário decida encerrar, 
    digitando '2'. Após o término da coleta de frases, a função utiliza a função `conta_palavras` para contar o número de palavras 
    em cada frase e imprime o resultado.

    Não recebe parâmetros e não retorna nenhum valor. O resultado é impresso diretamente no console.

    Exemplo de uso:
    - O usuário insere várias frases.
    - Ao finalizar com a escolha de encerrar (digitando 2), a função exibe o número de palavras de cada frase inserida.

    Exemplo interativo:
    >>> Digite uma frase para a história: "Era uma vez"
    >>> Digite 1 para adicionar outra frase ou 2 para encerrar: 1
    >>> Digite uma frase para a história: "um dragão feroz"
    >>> Digite 1 para adicionar outra frase ou 2 para encerrar: 2
    [3, 3]  # Saída representando o número de palavras nas frases inseridas.
    """

    historia = []
    while True:
        frase = input("Digite uma frase para a história: ")
        historia.append(frase)
        escolha = int(input("Digite 1 para adicionar outra frase ou 2 para encerrar "))
        if (escolha == 2):
            break
    print(conta_palavras(historia))

recebe_historia()

# EXERCÍCIO 4:
def conta_vogais(lista):
    """
    Conta o número de vogais (incluindo acentuadas e com til) em cada string de uma lista.

    Args:
        lista (list of str): Uma lista de strings nas quais as vogais serão contadas.

    Returns:
        list of int: Uma lista com o número de vogais encontradas em cada string da lista de entrada.

    Exemplos:
        >>> conta_vogais(['abacaxi', 'pão', 'gato'])
        [3, 2, 2]

    A função considera as seguintes vogais: 'a', 'e', 'i', 'o', 'u' (minúsculas e maiúsculas),
    além das vogais acentuadas ('á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â', 'ê', 'ô', 'à').

    Note:
        A contagem de vogais é feita de forma case-insensitive.
    """

    vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â', 'ê', 'ô', 'à']
    num_de_vogais = [sum(1 for char in x.lower() if char in vogais) for x in lista] # solução em apenas uma linha
    return num_de_vogais

frases = ["Hoje o dia estava ensolarado.", "Amanhã deve fazer sol também.", "Ontem e anteontem estava chuvoso ou nublado."]
print(conta_vogais(frases))

# EXERCÍCIO 5:
pessoas = {
    'Pedro': 18,
    'Maria': 15,
    'Ester': 21,
    'Francisco': 25,
    'Vitória': 10
}

def retorna_maior_idade(dicionario):
    """
    Filtra e retorna um novo dicionário contendo apenas os nomes e idades das pessoas 
    que possuem 18 anos ou mais.

    Parâmetros:
    dicionario (dict): Um dicionário onde as chaves são os nomes (strings) das pessoas 
                       e os valores são as idades (inteiros).

    Retorna:
    dict: Um novo dicionário contendo apenas as pessoas com idade maior ou igual a 18 anos.
    
    Exemplo:
    >>> retorna_maior_idade({'Ana': 20, 'João': 17, 'Maria': 22})
    {'Ana': 20, 'Maria': 22}
    """

    maior_idade = {nome: idade for nome, idade in dicionario.items() if idade >= 18}
    return maior_idade

print(retorna_maior_idade(pessoas))

# EXERCÍCIO 6:
def retira_palavras(texto, lista):
    """
    Remove palavras de um texto com base em uma lista de palavras a serem excluídas.

    Args:
        texto (str): O texto de entrada, contendo as palavras a serem filtradas.
        lista (list): Uma lista de palavras que devem ser removidas do texto.
                      As palavras são comparadas de forma case-insensitive.

    Returns:
        str: O texto resultante após a remoção das palavras presentes na lista.

    Exemplo:
        >>> retira_palavras("A casa é bonita", ["casa", "bonita"])
        "A é"
    """

    palavras = texto.split()
    palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in lista]

    return ' '.join(palavras_filtradas)

texto = "Botafogo flamengo fluminense vasco Corinthians palmeiras Santos"
palavras_indesejadas = ["flamengo", "fluminense", "vasco", "palmeiras"]

print(retira_palavras(texto, palavras_indesejadas))

# EXERCÍCIO 7:
def alterna_letras(texto):
    """
    Alterna as letras de uma string, deixando as letras nas posições
    pares (índices 0, 2, 4, ...) em maiúsculas e as letras nas posições
    ímpares (índices 1, 3, 5, ...) em minúsculas.

    Parâmetros:
    texto (str): A string de entrada na qual as letras serão alternadas.

    Retorna:
    str: Uma nova string com as letras alternadas conforme a regra descrita.

    Exemplo:
    >>> alterna_letras("exemplo")
    'ExEmPlO'
    
    >>> alterna_letras("testando")
    'TeStAnDo'
    """

    return ''.join(
        c.upper() if i % 2 == 0 else c.lower()
        for i, c in enumerate(texto)
    )

texto = "desenvolvendo habilidades"
print(alterna_letras(texto))

# EXERCÍCIO 8:
import itertools
def retorna_itens_unicos(lista):
    """
    Retorna uma lista com os elementos únicos de uma lista de listas, removendo duplicatas.

    A função recebe uma lista contendo outras listas (ou iteráveis) e retorna uma nova lista 
    contendo os elementos únicos, ou seja, sem repetições, de todos os itens presentes nas 
    listas internas. A ordem dos elementos no resultado final não é garantida, pois um 
    conjunto (`set`) é utilizado para eliminar duplicatas.

    Parâmetros:
    lista (list): Uma lista de listas (ou iteráveis), da qual os elementos serão extraídos e 
                  filtrados para que apenas os elementos únicos sejam retornados.

    Retorna:
    list: Uma lista com os elementos únicos extraídos das listas internas fornecidas.

    Exemplo:
    >>> retorna_itens_unicos([[1, 2, 3], [2, 3, 4], [4, 5]])
    [1, 2, 3, 4, 5]
    """

    elementos_unicos = list(set(itertools.chain(*lista)))
    return elementos_unicos

lista = [[2,4,6], [4, 5, 1, 6], [2, 2, 6]]
print(retorna_itens_unicos(lista))

# EXERCÍCIO 9:
def intercala_palavras(lista1, lista2):
    resultado = []
    tamanho_minimo = min(len(lista1), len(lista2))

    for i in range(tamanho_minimo):
        resultado.append(lista1[i])
        resultado.append(lista2[i])

    resultado.extend(lista1[tamanho_minimo:])
    resultado.extend(lista2[tamanho_minimo:])

    return ' '.join(resultado)

lista1 = ['eu', 'de', 'em']
lista2 = ['gosto', 'programar', 'python', 'todos', 'os', 'dias']
print(intercala_palavras(lista1, lista2))    

# EXERCÍCIO 10:
def retorna_listas(lista, numero):
    """
    Divide uma lista de strings em duas sublistas com base no comprimento dos elementos.

    A função recebe uma lista de strings e um número, e retorna uma lista contendo 
    duas sublistas:
    - A primeira sublista contém os elementos da lista original que possuem comprimento 
      menor ou igual ao número fornecido.
    - A segunda sublista contém os elementos da lista original que possuem comprimento 
      maior que o número fornecido.

    Parâmetros:
    lista (list of str): Lista de strings a ser dividida.
    numero (int): Número que serve como critério para dividir a lista com base no comprimento 
                  dos elementos.

    Retorna:
    list: Uma lista contendo duas sublistas:
          - A primeira sublista com elementos de comprimento menor ou igual a `numero`.
          - A segunda sublista com elementos de comprimento maior que `numero`.
          
    Exemplo:
    >>> retorna_listas(["banana", "uva", "pera", "abacate", "abacaxi"], 5)
    [['uva', 'pera'], ['banana', 'abacate', 'abacaxi']]

    """
    
    resultado = []

    comprimento_menor = [x for x in lista if len(x) <= numero]
    resultado.append(comprimento_menor)

    comprimento_maior = [x for x in lista if len(x) > numero]
    resultado.append(comprimento_maior)

    return resultado

palavras = ["banana", "uva", "pera", "abacate", "abacaxi"]
numero = 5

print(retorna_listas(palavras, numero))

# EXERCÍCIO 11:
def inserir_palavra(lista, palavra):
    """
    Insere uma palavra em uma lista em uma posição específica.

    A função solicita ao usuário a posição em que deseja inserir a nova palavra.
    Caso a lista tenha menos de 3 elementos, a palavra será adicionada ao final da lista.
    Caso contrário, a palavra será inserida na posição fornecida pelo usuário.

    Parâmetros:
    lista (list): A lista onde a palavra será inserida.
    palavra (str): A palavra a ser inserida na lista.

    Retorna:
    list: A lista atualizada com a palavra inserida na posição especificada.

    Exemplo:
    >>> inserir_palavra(["maçã", "banana"], "laranja")
    Digite de forma numérica a posição em que deseja inserir a nova palavra  # Suponha que o usuário digite 1
    ['maçã', 'banana', 'laranja']

    """
    posicao = int(input("Digite de forma numérica a posição em que deseja inserir a nova palavra "))

    if (len(lista) < 3):
        lista.append(palavra)
    else:
        lista.insert(posicao, palavra)    
    
    return lista

lista = ["abacate", "pera", "abacaxi"]
palavra = "uva"

print(inserir_palavra(lista, palavra))

# EXERCÍCIO 12:
def combinar_listas(lista1, lista2):
    """
    Combina duas listas, adicionando os elementos de `lista2` ao final de `lista1`.

    Args:
        lista1 (list): A primeira lista, que será modificada.
        lista2 (list): A segunda lista, cujos elementos serão adicionados à `lista1`.

    Returns:
        list: A lista resultante, que é a `lista1` com os elementos de `lista2` no final.

    Exemplo:
        >>> combinar_listas([1, 2], [3, 4])
        [1, 2, 3, 4]
    """

    lista1.extend(lista2)
    return lista1

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(combinar_listas(lista1, lista2))

# EXERCÍCIO 13:
def remover_duplicatas(lista):
    """
    Remove os elementos duplicados de uma lista, mantendo apenas os elementos únicos.

    Parâmetros:
    lista (list): A lista da qual os elementos duplicados serão removidos.

    Retorna:
    list: Uma nova lista contendo apenas os elementos únicos da lista original.
    
    Exemplo:
    >>> remover_duplicatas(["banana", "banana", "uva", "uva", "pera", "pera"])
    ["banana", "pera", "uva"]

    """
    elementos_unicos = list(set(lista))
    return elementos_unicos

lista = ["banana", "banana", "uva", "uva", "pera", "pera"]
print(remover_duplicatas(lista))

# EXERCÍCIO 14:
def gerenciar_compras(lista):
    """
    Gerencia a lista de compras removendo o último item.

    Esta função verifica se a lista de compras está vazia. Se estiver, retorna uma mensagem informando
    que não há mais itens para remover. Caso contrário, remove o último item da lista e retorna a lista
    atualizada.

    Parâmetros:
    lista (list): A lista de compras, que pode ser uma lista de itens a serem comprados.

    Retorna:
    list | str: A lista atualizada de compras após a remoção do último item, ou uma mensagem informando
               que não há mais itens para remover caso a lista esteja vazia.
    """

    if not lista:
        return "Não há mais itens para remover!"
    else:
        lista.pop()
        return lista
    
lista = ['camisa', 'tenis', 'bolsa']
print(gerenciar_compras(lista))  

# EXERCÍCIO 15:
def manipular_string(texto):
    """
    Exibe uma parte de uma string com base nos índices fornecidos pelo usuário.

    Esta função imprime o texto original, solicita ao usuário dois índices (início e fim),
    e exibe a substring correspondente à faixa entre os índices fornecidos.

    Parâmetros:
    texto (str): A string de entrada da qual será extraída a substring.

    Exemplo:
    >>> manipular_string("Olá, Mundo!")
    Digite um índice de início: 4
    Digite um índice de fim: 9
    Mundo

    """
    print(texto)
    indice_inicio = int(input("Digite um índice de início: "))
    indice_fim = int(input("Digite um índice de fim: "))
    substring = texto[indice_inicio:indice_fim]
    print(substring)

texto = "Python é incrível!"
manipular_string(texto)   

# EXERCÍCIO 16:
def gerenciar_lista_compras(lista_compras):
    """
    Função para gerenciar uma lista de compras interativamente, permitindo ao usuário:
    
    - Adicionar itens em uma posição específica na lista.
    - Remover itens da lista pelo nome ou índice.
    - Encerrar a gestão da lista.

    A função exibe a lista de compras a cada interação e solicita que o usuário insira um comando.
    O processo continua até que o comando 'fim' seja digitado.

    Parâmetros:
    lista_compras (list): Lista de produtos de compras, onde cada item é uma string representando um produto.

    Comandos válidos:
    - 'fim': Encerra a gestão da lista.
    - 'remover <índice/nome>': Remove um item da lista. Pode-se passar um índice numérico ou o nome do produto.
    - 'adicionar <índice> <nome do produto>': Adiciona um item na lista em uma posição específica.

    Exemplo de uso:
    lista = ["leite", "pão", "arroz"]
    gerenciar_lista_compras(lista)

    A função não retorna nada. Ela modifica a lista de compras diretamente.
    """
    while True:
        print("\nLista de compras atual:", lista_compras)
        comando = input("Digite um comando (fim, remover, adicionar): ").strip()

        if comando == "fim":
            print("Encerrando a gestão da lista de compras.")
            break

        elif comando.startswith("remover"):
            # Remover produto pela posição ou nome
            comando_remover = comando.split(" ", 1)
            if len(comando_remover) == 2:
                parametro = comando_remover[1].strip()

                if parametro.isdigit():
                    # Se for um número, remover pelo índice
                    indice = int(parametro)
                    if 0 <= indice < len(lista_compras):
                        removed = lista_compras.pop(indice)
                        print(f"Item '{removed}' removido.")
                    else:
                        print("Índice inválido.")
                else:
                    # Se não for número, tentar remover pelo nome
                    if parametro in lista_compras:
                        lista_compras.remove(parametro)
                        print(f"Item '{parametro}' removido.")
                    else:
                        print(f"Produto '{parametro}' não encontrado na lista.")
            else:
                print("Comando 'remover' inválido. Use 'remover <índice/nome>'.")

        elif comando.startswith("adicionar"):
            # Adicionar produto em um índice específico
            comando_adicionar = comando.split(" ", 2)
            if len(comando_adicionar) == 3:
                try:
                    indice = int(comando_adicionar[1].strip())
                    nome_produto = comando_adicionar[2].strip()

                    if 0 <= indice <= len(lista_compras):
                        lista_compras.insert(indice, nome_produto)
                        print(f"Produto '{nome_produto}' adicionado na posição {indice}.")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Índice inválido. Digite um número inteiro.")
            else:
                print("Comando 'adicionar' inválido. Use 'adicionar <índice> <nome do produto>'.")

        else:
            print("Comando desconhecido. Tente novamente.")
        
    # Exibir a lista final
    print("\nLista de compras final:", lista_compras)


# Exemplo de uso:
lista = ["leite", "pão", "arroz"]
gerenciar_lista_compras(lista)


