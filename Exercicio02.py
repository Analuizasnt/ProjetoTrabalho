print('Esse é o programa que verifica se o número digitado faz parte da sequência de fibonacci \n')
n = int(input('Agora digite o número que você deseja verificar: '))

listaFibonacci = [0, 1]

while listaFibonacci[-1] < n:
    listaFibonacci.append(listaFibonacci[-1] + listaFibonacci[-2])

print(
    'Foi feito o cálculo da lista de fibonacci até onde foi necessário para verificar se o número digitado faz parte, veja só a lista: \n')
print(listaFibonacci)

if n in listaFibonacci:
    print('Considerando a lista acima, o número faz parte da lista de fibonacci.')
else:
    print('Considerando a lista acima, o número não faz parte da lista de fibonacci.')