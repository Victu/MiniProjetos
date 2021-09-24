from random import randint
from time import sleep

print('=-' * 25)
print(f'{"> JOKENPÔ <":-^50}')
print('-=' * 25)
opções = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
nome = input('Seu nome/apelido: ').strip().capitalize()
vitória = derrota = 0

while True:
    print('=' * 50)
    print('Digite "0" - PEDRA\nDigite "1" - PAPEL\nDigite "2" - TESOURA')
    print('=' * 50)
    jogador = int(input(f'- {nome}, selecione um número: '))
    while jogador < 0 or jogador > 2:  # Entra nesse loop caso digite um número/opção inválida
        jogador = int(input('- Selecione uma opção válida: '))
    print('- Agora é a vez do PC...')
    sleep(1.5)
    print('-' * 50)
    print(f'{"JO":>16}', end='...  ')
    sleep(1)
    print('KEN', end='...  ')
    sleep(1)
    print('PÔ!!')
    sleep(1)
    print('-' * 50)
    print(f'{nome} escolheu: {opções[jogador]}')  # Imprime a escolha do jogador
    for o in range(len(opções)):
        if pc == o:
            print(f'O PC escolheu: {opções[o]}')  # Imprime a escolha da máquina
    print('- RESULTADO:', end=' ')
    if jogador == pc:
        print('Empate!')
        print('-' * 50)
    else:  # Essa condição é iniciada quando a escolha do jogador é diferente da máquina
        if jogador == 0 and pc == 2:
            print('Boa! Você venceu.')
            vitória += 1
        elif jogador == 2 and pc == 0:
            print('Ops... Não foi dessa vez...')
            derrota += 1
        if jogador == 1 and pc == 0:
            print(f'Parabéns, {nome}! Você venceu.')
            vitória += 1
        elif jogador == 0 and pc == 1:
            print('Você perdeu...')
            derrota += 1
        if jogador == 2 and pc == 1:
            print(f'Muito bem, {nome}!')
            vitória += 1
        elif jogador == 1 and pc == 2:
            print('Boa sorte na próxima vez.')
            derrota += 1
        print('=' * 50)
        print(f'{" PLACAR ":-^50}\n{"|PC:":>19} {derrota} x {nome}: {vitória}|')
        print('=' * 50)
    repetir = input('Quer repetir?[s/n] ').strip().lower()[0]
    while not repetir in 'SsNn':  # Esse loop é iniciado quando resposta for inválida
        repetir = input('Resposta inválida. Quer repetir?[s/n] ').strip().lower()[0]
    if repetir in 'Nn':
        print('Finalizando...')
        sleep(3)
        break
print('=-' * 25 + f'\n{"FIM DE JOGO":>30}.')
