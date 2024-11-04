#Ler uma lista de 10 números reais e mostre-os na ordem inversa.
numeros = []
for n in range(10):
    numero = float(input("digite o numero real"))
    numeros.append(numero)
numeros.reverse()
print(numeros)