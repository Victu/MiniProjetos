from random import randint
from time import sleep

print('=-' * 25)
print(f'{"> JOKENPÔ <":-^50}')
print('-=' * 25)
opções = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
nome = input('Seu nome/apelido: ').strip().capitalize()

while True:
    print('Digite "0" - PEDRA\nDigite "1" - PAPEL\nDigite "2" - TESOURA')
    jogador = int(input(f'{nome}, selecione um número: '))
    print('-' * 50)
    if jogador < 0 or jogador > 2:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')
        break
    print(f'{"JO":>16}', end='...  ')
    sleep(0.8)
    print('KEN', end='...  ')
    sleep(0.8)
    print('PÔ!!')
    sleep(0.8)
    print('-' * 50)
    print(f'{nome} escolheu: {opções[jogador]}')
    for o in range(len(opções)):
        if pc == o:
            print(f'O PC escolheu: {opções[o]}')
            print('-' * 50)
    print('- RESULTADO:', end=' ')
    if jogador == pc:
        print('Empate!')
    else:
        if jogador == 0 and pc == 2:
            print('Você venceu! Continue assim.')
        elif jogador == 2 and pc == 0:
            print('Ops... Não foi dessa vez...')
        if jogador == 1 and pc == 0:
            print('Parabéns! Você venceu.')
        elif jogador == 0 and pc == 1:
            print('Você perdeu...')
        if jogador == 2 and pc == 1:
            print('Boa! Você venceu.')
        elif jogador == 1 and pc == 2:
            print('Boa sorte na próxima vez.')
    print('-' * 50)
    repetir = input('Quer repetir?[s/n] ').strip().lower()[0]
    while not repetir in 'SsNn':
        repetir = input('resposta inválida. Quer repetir?[s/n] ').strip().lower()[0]
    if repetir in 'Nn':
        break

print('=-' * 25 + '\nFIM DE JOGO.')
