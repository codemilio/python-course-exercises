# Python é CaseSensitive, ou seja:

nome_completo = "Evandro Ivanilson"

# é diferente de: 

nome_Completo = ""

"""
  Existem alguns padrões de declaração:

  snake_case: para funções e métodos 
  camelCase: para clases
  kebab-case: para nome de arquivos 
  PascalCase

  ref: https://peps.python.org/pep-0008/
"""

# Tipos de variáveis 
value_a = 4 # Inteiros 
value_b = 3.14 # Real com ponto flutuante 

# type() 
print("Classe pré-definida para inteiro = ", type(value_a))
print("Classe pré-definida para ponto flutuante = ", type(value_b))

# texto com quebra
paragraphy_a = """
  lorem ipsom
  elson alseiunm
"""

paragraphy_b = "lorem \
  ipsum"

# Formatações
print("nome completo:", nome_completo) # adiciona espaço automaticamente entre o ultimo caractere e a variável
print("nome completo concatenado: " + nome_completo) # não adiciona espaço
print("nome completo", nome_completo + "-4") # podemos usar os dois métodos juntos 
print("texto com quebra:", paragraphy_a)
print("texto sem quebra:", paragraphy_b)

nome = "Carlos"
sobrenome = "Silva"
print("nome completo: %s %s" % (nome, sobrenome)) # faz a transformação das variáveis pra string

# F-String (utilizar variáveis dentro de texto) 
print(f"Nome: {nome} {sobrenome}")
print("Nome: {} {}".format(nome, sobrenome))


