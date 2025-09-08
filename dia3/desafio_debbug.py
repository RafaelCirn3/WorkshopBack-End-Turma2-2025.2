# main.py
# -------------------------------------------------------------
# Treinando resolução de problemas — Soluções comentadas
# Cada exercício abaixo contém:
#   1) O código corrigido (robusto e executável)
#   2) Uma explicação logo abaixo, como comentários
# No final há um "main()" que demonstra cada solução sem exigir entradas.
# -------------------------------------------------------------

from typing import Any, Iterable, List, Optional


# =============================================================
# ✅ NÍVEL 1 — FÁCIL
# =============================================================

# -------------------------------------------------------------
# Exercício 1 — Identificando um Erro de Sintaxe
# Código original (com erro): print("Olá, mundo!"
# Correção:
def ex1_ola_mundo() -> None:
    print("Olá, mundo!")

# Explicação:
# O erro era um SyntaxError causado pela falta do parêntese de fechamento.
# Em Python, chamadas de função precisam abrir e fechar parênteses.


# -------------------------------------------------------------
# Exercício 2 — Lidando com um NameError
def ex2_imprimir_nome() -> str:
    # Correção: definir a variável antes de usá-la.
    nome = "Rafael"  # exemplo; poderia vir de input() ou de outra fonte
    msg = f"Nome definido: {nome}"
    print(msg)
    return msg

# Explicação:
# O erro NameError ocorre quando o nome/variável não existe no escopo atual
# (a variável ainda não foi definida). A correção é garantir que a variável
# seja criada (atribuída) antes do acesso.


# =============================================================
# ✅ NÍVEL 2 — MÉDIO
# =============================================================

# -------------------------------------------------------------
# Exercício 3 — Erro de Tipagem (TypeError)
def somar_robusto(a: Any, b: Any) -> float:
    """
    Tenta somar 'a' e 'b' sem alterar a chamada original.
    Estratégia:
      1) Tenta a soma direta (funciona se os tipos forem compatíveis).
      2) Em caso de TypeError, converte para float quando possível.
      3) Se ainda falhar, lança um TypeError explicativo.
    """
    try:
        return a + b  # pode funcionar (ex.: números, ou até strings)
    except TypeError:
        try:
            return float(a) + float(b)
        except (TypeError, ValueError):
            raise TypeError(f"Não foi possível somar {type(a).__name__} e {type(b).__name__}.")

def ex3_demo() -> float:
    resultado = somar_robusto(10, "5")
    print(f"Ex3 — Resultado da soma robusta: {resultado}")
    return resultado

# Explicação:
# O erro era: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# (não é possível somar int com str). A solução captura o TypeError e tenta
# converter os valores para float, mantendo a chamada somar(10, "5").


# -------------------------------------------------------------
# Exercício 4 — Corrigindo um Erro de Índice (IndexError)
def obter_elemento_por_indice(numeros: List[int], indice: Any) -> Optional[int]:
    """
    Valida e retorna o elemento do índice solicitado.
    - Rejeita índices não inteiros e negativos.
    - Garante que o índice esteja dentro de [0, len(numeros)-1].
    - Usa try/except para evitar que o programa quebre.
    Retorna o elemento ou None quando inválido.
    """
    try:
        idx = int(indice)
    except (TypeError, ValueError):
        print("Índice inválido: digite um número inteiro.")
        return None

    if idx < 0 or idx >= len(numeros):
        print(f"Índice fora do intervalo permitido (0 a {len(numeros)-1}).")
        return None

    try:
        valor = numeros[idx]
        print(f"Elemento no índice {idx}: {valor}")
        return valor
    except IndexError:
        # Defesa adicional (embora a checagem de faixa já evite isso)
        print("Erro: índice fora dos limites da lista.")
        return None

def ex4_demo() -> List[Optional[int]]:
    numeros = [10, 20, 30]
    testes = ["a", -1, 0, 2, 3]
    print("Ex4 — Testando acesso por índice com entradas variadas:", testes)
    resultados = [obter_elemento_por_indice(numeros, t) for t in testes]
    return resultados

# Explicação:
# O código original quebrava por:
# - ValueError ao converter entradas não numéricas com int(input(...)).
# - IndexError ao acessar um índice fora da faixa da lista.
# A correção valida o tipo e a faixa do índice e usa try/except para
# tratar erros graciosamente, incluindo rejeitar índices negativos.


# -------------------------------------------------------------
# Exercício 5 — Tratando múltiplos erros ao mesmo tempo
def dividir(a: float, b: float) -> float:
    return a / b

def dividir_com_tratamento(num1_str: str, num2_str: str) -> Optional[float]:
    """
    Converte entradas para float e divide com tratamento de erros:
      - ValueError: entradas não numéricas
      - ZeroDivisionError: divisão por zero
      - TypeError: entradas inesperadas
    Retorna o resultado ou None se houver erro (com mensagem amigável).
    """
    try:
        a = float(num1_str)
        b = float(num2_str)
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")
        return resultado
    except ValueError:
        print("Erro: você deve digitar números válidos (ex.: 10, 3.5).")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    except TypeError:
        print("Erro: tipos inválidos recebidos.")
    return None

def ex5_demo() -> List[Optional[float]]:
    print("Ex5 — Demonstração com várias entradas:")
    casos = [("10", "2"), ("x", "3"), ("4", "0"), ("5.5", "2.2")]
    resultados = []
    for a, b in casos:
        print(f" Tentando dividir {a} por {b} -> ", end="")
        resultados.append(dividir_com_tratamento(a, b))
    return resultados

# Explicação:
# Possíveis erros:
# - ValueError: quando o usuário insere texto em vez de número.
# - ZeroDivisionError: quando o segundo número é zero.
# - TypeError: quando os tipos recebidos não são os esperados.
# A solução converte entradas para float e captura cada erro com uma
# mensagem clara, evitando a quebra do programa.


# =============================================================
# ✅ NÍVEL 3 — DIFÍCIL
# =============================================================

# -------------------------------------------------------------
# Exercício 6 — Erro ao trabalhar com dicionários
def acessar_dict_com_tratamento(dados: dict, chave: str) -> Optional[Any]:
    """
    Tenta acessar dados[chave] com tratamento de erro.
    Também mostra como usar get() para fornecer um padrão amigável.
    """
    try:
        valor = dados[chave]
        print(f"O valor da chave '{chave}' é: {valor}")
        return valor
    except KeyError:
        padrao = dados.get(chave, "Chave não encontrada (via get()).")
        print(f"Chave inexistente. Retornando padrão: {padrao}")
        return None

def ex6_demo() -> List[Optional[Any]]:
    dados = {"nome": "Isaac", "idade": 25, "cidade": "São Paulo"}
    testes = ["nome", "idade", "endereco", "cidade"]
    print("Ex6 — Testando acesso a chaves:", testes)
    resultados = [acessar_dict_com_tratamento(dados, t) for t in testes]
    # Exemplo explícito de get():
    exemplo_get = dados.get("endereco", "Endereço não encontrado (via get()).")
    print("Ex6 — Exemplo com get():", exemplo_get)
    return resultados

# Explicação:
# Acesso a uma chave inexistente gera KeyError. Com try/except, tratamos o
# erro e podemos fornecer mensagens amigáveis. O método dict.get(chave, padrao)
# evita o erro, retornando o valor da chave se existir ou o padrão fornecido.


# -------------------------------------------------------------
# Exercício 7 — Criando um erro personalizado (validação de idade)
class IdadeInvalidaError(ValueError):
    """Erro específico para idades fora do intervalo permitido."""

def validar_idade(idade: int) -> str:
    if idade < 0 or idade > 120:
        # Lançamos um erro específico (derivado de ValueError)
        raise IdadeInvalidaError("A idade deve estar entre 0 e 120 anos!")
    return f"Idade válida: {idade}"

def solicitar_idade_valida(entradas: Iterable[Any]) -> Optional[str]:
    """
    Simula múltiplas tentativas de entrada até uma idade válida ser fornecida.
    Recebe um iterável de entradas (para teste sem input()) e retorna a mensagem.
    """
    for tentativa in entradas:
        try:
            idade = int(tentativa)
            msg = validar_idade(idade)
            print(msg)
            return msg
        except (TypeError, ValueError):
            print("Entrada inválida: digite um número inteiro.")
        except IdadeInvalidaError as e:
            print(f"Erro de validação: {e}")
    print("Não foi possível obter uma idade válida nas tentativas fornecidas.")
    return None

def ex7_demo() -> List[Optional[str]]:
    print("Ex7 — Testando validador de idade com entradas inválidas e válidas.")
    casos = [[-5, 130, "x", 40], [25]]
    resultados = []
    for seq in casos:
        print(f"  Tentativas: {seq}")
        resultados.append(solicitar_idade_valida(seq))
    return resultados

# Explicação:
# Corrigimos a sintaxe da função (faltava ':') e adicionamos um loop de tentativas
# simuladas para continuar pedindo até obter uma idade válida.
# Lançamos um erro específico (IdadeInvalidaError) ao invés de ValueError genérico
# e capturamos tanto entradas não numéricas quanto idades fora do intervalo.


# =============================================================
# 💡 DESAFIO EXTRA — Debugando um código com múltiplos erros
# =============================================================
def calcular_media_segura(notas: Iterable[Any]) -> float:
    """
    Converte as notas para float e calcula a média com validações.
    - Rejeita notas não numéricas
    - Rejeita lista vazia
    """
    coerced: List[float] = []
    for n in notas:
        try:
            coerced.append(float(n))
        except (TypeError, ValueError):
            raise ValueError(f"Nota inválida: {n!r}. Use apenas números.")
    if not coerced:
        raise ValueError("Lista de notas vazia. Informe ao menos uma nota.")
    return sum(coerced) / len(coerced)

def ler_notas_de_string(entrada: str) -> List[float]:
    """
    Aceita uma string com notas separadas por espaço ou vírgula e retorna uma lista de floats.
    Ex.: '8 9 10 7' ou '8,9,10,7'
    """
    if not entrada or not entrada.strip():
        raise ValueError("Entrada vazia.")
    # Normaliza separadores
    entrada = entrada.replace(",", " ")
    partes = [p for p in entrada.split() if p.strip()]
    return [float(p) for p in partes]

def ex_desafio_demo() -> float:
    # Corrigindo a lista original que continha uma string "10" (que agora é tratada)
    notas = [8, 9, "10", 7]
    media = calcular_media_segura(notas)
    print(f"Desafio — Média: {media:.2f}")
    # Demonstração de leitura a partir de uma "entrada do usuário" simulada:
    entrada_usuario = "6.5, 7, 8, 9"
    notas_usuario = ler_notas_de_string(entrada_usuario)
    media_usuario = calcular_media_segura(notas_usuario)
    print(f"Desafio — Média (usuário): {media_usuario:.2f}")
    return media

# Explicação:
# Problemas no código original:
# 1) A lista tinha uma string "10". sum([8, 9, "10", 7]) gera TypeError.
# 2) Formatação {media:.2f} exige número; se a média fosse None ou inválida, quebraria.
# 3) Lista vazia geraria ZeroDivisionError ao dividir por zero.
# Correções:
# - Convertemos todas as notas para float e validamos a lista.
# - Lançamos mensagens claras para entradas inválidas.
# - Fornecemos função para ler notas de string (simulando entrada do usuário).


# =============================================================
# Função principal que demonstra todas as soluções sem entradas reais
# =============================================================
def main() -> None:
    print("\n=== Nível 1 ===")
    ex1_ola_mundo()
    ex2_imprimir_nome()

    print("\n=== Nível 2 ===")
    ex3_demo()
    ex4_demo()
    ex5_demo()

    print("\n=== Nível 3 ===")
    ex6_demo()
    ex7_demo()

    print("\n=== Desafio Extra ===")
    ex_desafio_demo()


if __name__ == "__main__":
    main()
