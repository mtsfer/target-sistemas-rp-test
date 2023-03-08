# 1) Soma - Resposta: 91
print('1) ', end='')
indice, soma, k = 13, 0, 0
while k < indice:
    k += 1
    soma += k
print(soma)

# 2) Sequência de Fibonacci:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
print('2) ', end='')
number = int(input('Digite um número: '))

firstFibonacciNumber = 0
secondFibonacciNumber = 1
nextFibonacciNumber = 1

isNumberFoundOnSequence = True if number in (0, 1) else False
while nextFibonacciNumber < number and not isNumberFoundOnSequence:
    firstFibonacciNumber = secondFibonacciNumber
    secondFibonacciNumber = nextFibonacciNumber
    nextFibonacciNumber = firstFibonacciNumber + secondFibonacciNumber
    if nextFibonacciNumber == number:
        isNumberFoundOnSequence = True

if isNumberFoundOnSequence:
    print(f'O número {number} faz parte da Sequência de Fibonacci!')
else:
    print(f'O número {number} NÃO faz parte da Sequência de Fibonacci!')

"""
3) Lógica:
a) 1, 3, 5, 7, 9 (Números naturais ímpares positivos)
b) 2, 4, 8, 16, 32, 64, 128 (Potências de 2)
c) 0, 1, 4, 9, 16, 25, 36, 49 (Quadrado dos números naturais não negativos)
d) 4, 16, 36, 64, 100 (Quadrado dos números naturais pares positivos)
e) 1, 1, 2, 3, 5, 8, 13 (Recorte da Sequência de Fibonacci)
f) 2, 10, 12, 16, 17, 18, 19, 200 (Sequência de números que começam com a letra D)
"""

"""4) Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de 
Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a 
Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a 
cidade de Ribeirão Preto?


a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.  

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro 
possui tag de pedágio (Sem Parar).

c) Explique como chegou no resultado.

SOLUÇÃO: O enunciado não está muito claro. Ao se encontrarem, ambos os corpos estarão a uma mesma distância de 
ambas as cidades. Porém, podemos determinar o ponto de encontro entre eles:
  
Como queremos saber a distância para Ribeirão Preto, podemos considerar a trajetória iniciando de Franca.

Tendo em vista que a velocidade média do caminhão informada desconsidera o tempo parado, temos que calcular sua nova
velocidade média considerando os obstáculos.

S = 0 + 80t
100 = 80t
t = 100/80 = 1.25h (tempo em horas desconsiderando as paradas)

tp = 10/60
tp = 1/6 = 0.17h (tempo parado em horas)

tf = 1.25 + 0.17
tf = 1.42h (tempo total do deslocamento)

Vm = s/t
Vm = 100 / 1.42
Vm = 70.42km/h (velocidade média do caminhão considerando as paradas)

Agora, devemos calcular as funções horárias dos automóveis:
Caminhão: S1 = 0 + 70.42t
Carro = S2 = 100 - 110t

Ponto de encontro: S1 = S2
70.42t = 100 - 110t
180.42t = 100
t = 100 / 180.42
t = 0.55h (tempo de encontro dos automóveis)

Substituindo em qualquer das funções horárias:
S1 = 70.42 * 0.55
S1 = 38.73km

Portanto, ambos estarão a APROXIMADAMENTE 38.73km da origem da trajetória (Franca), representando 
APROXIMADAMENTE 61.27km de distância da cidade de Ribeirão Preto.
"""

# 5) Escreva um programa que inverta os caracteres de um string.
print('5) ', end='')
text = input('Digite uma frase: ')
reversedText = ''
for index in range(len(text) - 1, -1, -1):
    reversedText += text[index]
print(f'O texto invertido é: {reversedText}')
