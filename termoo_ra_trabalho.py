import random
import os

# ******************** FUNÇÕES *************************************

def colorir(text, color='default'):
    color_codes = {
        'default': '\033[0m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m'
    }
    return f"{color_codes[color]}{text}{color_codes['default']}"

def pintarPalavra(palavraGuess, palavraChave):
   # palavra com tamanho errado
   if len(palavraGuess) != len(palavraChave):  
      print("Tamanho não aceito")
      return False

   # salva valores para altera-los
   tempGuess = palavraGuess
   tempChave = palavraChave

   # cria uma lista com valores inicializados
   palavraPintada = ["" for i in palavraGuess]

   # checa as certas primeiro
   for i, char in enumerate(palavraGuess):
      # se encontrar o caracter
      if char == palavraChave[i]:
         # adiciona ele com a cor correspondente
         palavraPintada[i] = colorir(char, "green")
         # retira o caracter das palavras temporarias
         tempGuess = tempGuess[:i] + " " + tempGuess[i+1:]
         tempChave = tempChave[:i] + " " + tempChave[i+1:]

   # retira os caracteres vazios
   tempGuess = tempGuess.replace(" ", "")
   tempChave = tempChave.replace(" ", "")

   # agora checamos apenas o resto das palavras
   for i, char in enumerate(tempGuess):
      index = i
      # busca um index livre para colocar a próxima letra
      while(palavraPintada[index] != ""):
         index += 1

      # se ela existe na palavra -> amarelo senão -> vermelho
      if char in tempChave:
         palavraPintada[index] = colorir(char, "yellow")
      else:
         palavraPintada[index] = colorir(char, "red")
   
   dicas.append("".join(palavraPintada))
   return True

def printaDicas():
   for palavra in dicas:
      print(palavra)


# ******************** LEITURA DE ARQUIVO *************************************

listaPalavras = []

with open('palavras_termo.csv', encoding='utf8') as arquivo:
        for linha in arquivo:
            linha = linha.rstrip()
            palavras = linha.split(';')
            palavra = palavras[0]
            listaPalavras.append(palavra.lower())

# ******************** VARIAVEIS *************************************

palavraChave = listaPalavras[random.randint(0, len(listaPalavras))]
dicas = []
maxTentativas = 6
tentativas = maxTentativas

# ******************** MAIN *************************************



while(True):
   os.system("cls")

   if tentativas == 0:
      print("Acabaram suas tentativas ;-;")
      print(f"A palavra correta era: {palavraChave.upper()}")
      break

   print(f"Tamanho da palavra: {len(palavraChave)}")
   print(f"Tentativas restantes: {tentativas}")
   printaDicas()

   palavraDigitada = input("Digite: ")
   palavraDigitada = palavraDigitada.lower()

   # checa se houve um erro ao pintar a palavra
   if not pintarPalavra(palavraDigitada, palavraChave):
      continue

   tentativas -= 1

   if palavraDigitada == palavraChave:
      printaDicas()
      print(f"Você acertou em {maxTentativas - tentativas} tentativas")
      break
   