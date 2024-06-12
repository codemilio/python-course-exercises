nome_completo = "Evandro Ivanilson"
nome = "Carlos"
sobrenome = "Silva"

# upper() - converte os caracteres para upperCase 
print(nome.upper())

# Minusculo 
print(nome.lower())

# Imutabilidade - Observe que as variáveis declaradas não podem ser modificadas 

# count()
print(f"quantidade de A em {nome_completo}:", nome_completo.count("a"))

# find()
print(f"posição de A em {sobrenome.upper()}:", sobrenome.find("a"))

# replace() - altera todas as ocorrências 
print(f"troca A por O em {sobrenome.upper()}: ", sobrenome.replace("a", "o"))

# join() - adiciona um separador 
print(" ".join(nome.upper()))

# split() - divide uma string em uma lista/array 
print(nome_completo.split())

# strip() - remove um caractere alvo do começo e final da string 
# rstrip() - remove o caractere a direita (final) da string 
# lstrip() - remove o caractere a esquerda (inicio) da string 
dirt_string = "xCarlos Silvax"
print(f"input: {dirt_string}", "output:", dirt_string.strip("x")) 

# startwith() - verifica se uma string começa com uma determinadas sequência de caracteres e retorna um bool 
print(dirt_string.startswith("x"))
