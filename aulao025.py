import vazamentos


# variaveis = armazenar e reusar dados
# tipos de dados = string, integer, float, boolean

##variaveis
# nome = "Rodrigo" (str)
# idade = 18 (int)
# altura = 1.80 (float)
# peso = "80" (str)
# tem_filhos = false (bool)

#sequence matters


# a = 10
# b = 20
# a = 5

# print(a+b)

# alvo = 50
# print(alvo)
# print(type(alvo))
# print(type(type(alvo)))

##operadores
# + - * /
# // divisão inteira
# ** potencia
# % resto da divisão
# + cocatena strins 
#  "bruno" + "silva" = "brunosilva"

# print(10/3)

##listas
# lista = [1,2,3,4,5]

# 30 alvos
# alvos = ["terra.com", "google.com", "tecnicasdeinvasao]

# #########alvos = [
#     "google.com.br",
#     "facebook.com.br",
#     "amazon.com.br",
#     "uol.com.br",
#     "globo.com.br",
#     "mercadolivre.com.br",
#     "wikipedia.com.br",
#     "olx.com.br",
#     "netflix.com.br",
#     "instagram.com.br",
#     "itau.com.br",
#     "bb.com.br",
#     "caixa.gov.br",
#     "correios.com.br",
#     "magazineluiza.com.br",
#     "americanas.com.br",
#     "ifood.com.br",
#     "submarino.com.br",
#     "msn.com.br",
#     "yahoo.com.br",
#     "microsoft.com.br",
#     "apple.com.br",
#     "claro.com.br",
#     "vivo.com.br",
#     "oi.com.br",
#     "tim.com.br",
#     "bradesco.com.br",
#     "santander.com.br",
#     "extra.com.br",
#     "casasbahia.com.br",
#     "pontofrio.com.br",
#     "saraiva.com.br",
#     "estadao.com.br",
#     "folha.uol.com.br",
#     "terra.com.br",
#     "abril.com.br",
#     "globoesporte.com.br",
#     "veja.abril.com.br",
#     "g1.globo.com",
#     "r7.com",
#     "band.uol.com.br",
#     "sbt.com.br",
#     "recordtv.r7.com",
#     "tripadvisor.com.br",
#     "booking.com.br",
#     "decolar.com",
#     "airbnb.com.br",
#     "cvc.com.br",
#     "buscape.com.br",
#     "zoom.com.br",
#     "mercadopago.com.br",
#     "pagseguro.uol.com.br",
#     "nubank.com.br",
#     "picpay.com",
#     "getnet.com.br",
#     "stone.com.br",
#     "cielo.com.br",
#     "kabum.com.br",
#     "americanas.com",
#     "cnova.com",
#     "ricardoeletro.com.br",
#     "shopfacil.com.br",
#     "shoptime.com.br",
#     "brastemp.com.br",
#     "consul.com.br",
#     "electrolux.com.br",
#     "dell.com.br",
#     "asus.com.br",
#     "lenovo.com.br",
#     "samsung.com.br",
#     "lg.com.br",
#     "sony.com.br",
#     "motorola.com.br",
#     "xiaomi.com.br",
#     "hp.com.br",
#     "epson.com.br",
#     "canon.com.br",
#     "nikon.com.br",
#     "adobe.com.br",
#     "autodesk.com.br",
#     "symantec.com.br",
#     "kaspersky.com.br",
#     "avast.com.br",
#     "locaweb.com.br",
#     "hostgator.com.br",
#     "kinghost.com.br",
#     "uolhost.uol.com.br",
#     "terraempresas.com.br",
#     "wix.com.br",
#     "weebly.com",
#     "wordpress.com",
#     "blogger.com.br",
#     "shopify.com.br",
#     "magento.com.br",
#     "prestashop.com",
#     "vtex.com.br",
#     "tray.com.br",
#     "linx.com.br",
#     "tokstok.com.br",
#     "leroymerlin.com.br"
# ]
#posição na lista
#lista.funcao()

# print(alvos[0])
# terra.com
#print(alvos[1])

#função de uma lista
#print(len(alvos))
#9

#adicionar um elemento na lista
#alvos.append("globo.com")

#saber se há um elemento na lista
#print("glob.com" in alvos)
# false


##dicinarios
#alvos = [{'dominio': "terra.com.br", 'sistema':
 # variaveis dentro da variaavel, chaves, um atributo
#um objeto

# 'ip': "8.8.8.8"}, {'dominio': "tecnicasdeinvasao.com", 'sistema': "Linux", 'ip': "8.8.4.4"}, {'dominio': "globo.com", 'sistema': "Windows", 'ip': "8.8.8.8"}, {'dominio': "ig.com", 'sistema': "Mac", 'ip': "8.8.8.8"}, {'dominio': "fbi.gov", 'sistema': "Linux", 'ip': "8.8.8.8"}, {'dominio': "twitter.com", 'sistema': "Mac", 'ip': "8.8.8.8"}, {'dominio': "instagram.com", 'sistema': "Linux", 'ip': "8.8.8.8"}, {'dominio': "tiktok.com", 'sistema': "Windows", 'ip': "8.8.8.8"}]

####### alvo = {
#   "nome": "Bruno Fraga",
#   "cpf": "123.456.789-00",
#   "email": "qpmzj@example.com"
# }

# print(type(alvo))
# print(alvo)

# print("-"*10)
  
# #adicionar um atributo
# alvo["cidade"] = "Rio de Janeiro"
# print(alvo)

# print("-"*10)

# #atualizar um atributo
# alvo["email"] = "qpmz@example.com"
# print(alvo)

# print("-"*10)

# #deletar um atributo
# del alvo["cpf"]
# print(alvo)

# print("-"*10)

# #ler um atributo
# print(alvo["email"])

# print("-"*10)

# #ler todos os atributos, somente as chaves
# print(alvo.keys())

# print("-"*10)

# #ler todos os valores
# print(alvo.values())

# print("-"*10)

# #ler todos os atributos e valores
# print(alvo.items())

# print("-"*10)

# #ler todos os atributos e valores formatado
# for key, value in alvo.items():
#   print(f"A chave é {key} e o valor é {value}")


# print("-"*10)

########### alvo = [
#   {"nome": "Bruno", "cpf": "1111111", "email": "bruno@example.com"}, 
#   {"nome": "Pedro", "cpf": "55555555", "email": "pedro@example.com"}, 
#   {"nome": "Lucas", "cpf": "0000000", "email": "lucas@example.com"}
# ]

#print(alvo[0]["nome"])
#Bruno

##loop
#basicamente sua capacidade de interagir com cada item da sua lista separadamente

# for alvo in alvos:
#   print(alvo)
# print("-"*10)
# for alvo in alvos:
#   print("atacando ->", alvo["dominio"])
# print("-"*10)
# for alvo in alvos:
#   if alvo["sistema"] == "Windows":
#      print("atacando ->", alvo["dominio"])
# print("-"*10)


##Função
#é um bloco de código que executa uma tarefa específica

# def fazer_login(email, senha):
#   print("bem vindo")
#   print("usuario " + email)
# fazer_login("qpmzj@example.com", "123")
# def fazer_login(email, senha):
#   return

# ela é algo que tem como objetivo deixar o seu código modular

#função na mat: f(x) = x**2[definição da função ou def]


# nomeseu = "gustavo"
# print("olá")
# print(nomeseu)
# print("Hoje vc se fudeu")
#|
#|
#|
#V
#em uma função ficaria assim

# def boas_vindas(name):
#   print("olá")
#   print(name)
#   print("Hoje vc se fudeu")
# #name = argumento, variavel dentro da função

# boas_vindas("gustavo")
# boas_vindas("pedro")


##verificar vazamentos
 #está no módulo vazamentos.py
   # def verifica_vazamento(email):
   #   print("iniciando verificacao de vazamento")
   #   print(email)
   #   print("não tem vazamento")
   #   print("#####")

alvos = [
  {"nome": "Bruno", "cpf": "1111111", "email": "bruno@example.com"}, 
  {"nome": "Pedro", "cpf": "55555555", "email": "pedro@example.com"}, 
  {"nome": "Lucas", "cpf": "0000000", "email": "lucas@example.com"}
]

# print(alvo[0])
# #1º item isolado

# print(alvo[0]["email"])
# #filtrando o email

# for alvo in alvos:
#   print(alvo["nome"])
#   print("####")

for alvo in alvos:
  pega_email = alvo["email"]
  vazamentos.verifica_google(pega_email)
  #verifica_vazamento(alvo["email"])


##modulos
#é um arquivo que contém funções, classes, variáveis, etc.
#podem ser importados em outros arquivos
# import requests

#PyPI.org 
#lugar onde compartilha pacotes, que são um conjunto de módulos