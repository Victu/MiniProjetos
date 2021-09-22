from random import randint
from time import sleep
print('=-' * 25)
print(f'{"> JOKENPÔ <":-^50}')
print('-=' * 25)
print('''PEDRA - Digite "1"
PAPEL - Digite "2"
TESOURA - Digite "3"''')
opções = ('', 'PEDRA', 'PAPEL', 'TESOURA')
pc = randint(1, 3)
jogador = int(input('Selecione um número: '))

print('-' * 50)
for o in range(len(opções)):
    if jogador < 1 or jogador > 3:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')
        break
    if jogador == o:
        print('JO', end='...  ')
        sleep(0.8)
        print('KEN', end='...  ')
        sleep(0.8)
        print('PÔ!!')
        sleep(0.8)
        print('=' * 35)
        print(f'Você escolheu: {opções[o]}')
    if pc == o:
        print(f'O PC escolheu: {opções[o]}')
        print('=' * 35)
if jogador == pc:
    print('Houve um empate!')
else:
    if jogador == 1 and pc == 3:
        print('Muito bem! continue assim!')
    elif jogador == 3 and pc == 1:
        print('Ops... Não foi dessa vez...')
    if jogador == 2 and pc == 1:
        print('Parabéns! Você venceu.')
    elif jogador == 1 and pc == 2:
        print('Você perdeu...')
    if jogador == 3 and pc == 2:
        print('Boa!')
    elif jogador == 2 and pc == 3:
        print('Dessa vez, você perdeu... Tente novamente.')
print('=-' * 25 + '\nFIM DE JOGO.')
