''' Este programa implementa o crivo de Eratóstenes, que permite encontrar todos
os números primos entre dois números ou de 1 até um determinado valor limite.'''

def criar_lista(numeros):
    for i in range(numeros):
        minha_lista.append(i+1)
    return

def verificar_numero_primo(numero):
    num_divisores = 0
    divisor = 1
    while (divisor <= numero):
        if (numero%divisor == 0):
            num_divisores = num_divisores+1
        divisor = divisor+1
    if (num_divisores == 2):
        return 1
    else:
        return 0

def remover_multiplos_numero_primo(numero, numeros):
    for i in range(numero, numeros//numero):
        index = numero*i-1
        minha_lista[index] = "X"
    return

def remover_caracter_X():
    index = 0
    while (index <= len(minha_lista)-1):
        if (minha_lista[index] == "X"):
            del minha_lista[index]
        else:
            index += 1
    return
        
numeros = int(input("Quantos números inteiros contém o seu crivo de Eratóstenes? "))
minha_lista = list()
criar_lista(numeros)
print(minha_lista)
for i in range(numeros):
  if (minha_lista[i] != "X"):
      if (verificar_numero_primo(minha_lista[i])):
          remover_multiplos_numero_primo(minha_lista[i], numeros)
      else:
          minha_lista[i] = "X"
print("\n\n", minha_lista)
remover_caracter_X()
print("\n\n", minha_lista)
print("\nO seu crivo contém {} números primos" .format(len(minha_lista)))
