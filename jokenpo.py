from random import randint
from time import sleep

print('=-' * 25)
print(f'\033[1m{"> JOKENPÔ <":-^50}\033[m')
print('-=' * 25)
opções = ('\033[1;36mPEDRA\033[m', '\033[1;34mPAPEL\033[m', '\033[1;35mTESOURA\033[m')
nome = input('Seu nome/apelido: ').strip().capitalize()
vitória = derrota = 0

while True:  # Começo
    print('=' * 50)
    print(f'Digite "0" - {opções[0]}\nDigite "1" - {opções[1]}\nDigite "2" - {opções[2]}')
    print('=' * 50)
    jogador = int(input(f'- {nome}, selecione um número: '))
    pc = randint(0, 2)
    while jogador < 0 or jogador > 2:  # Entra nesse loop caso digite um número/opção inválida
        jogador = int(input('- \033[31mSelecione uma opção válida: \033[m'))
    print('- Agora é a vez do PC...')
    sleep(1.5)
    print('-' * 50)
    print(f'\033[36m{"JO":>16}', end='...  \033[m')
    sleep(1)
    print('\033[34mKEN', end='...  \033[m')
    sleep(1)
    print('\033[35mPÔ!!\033[m')
    sleep(1)
    print('-' * 50)
    print(f'\033[33m{nome} escolheu:\033[m {opções[jogador]}')  # Imprime a escolha do jogador
    for o in range(len(opções)):
        if pc == o:
            print(f'\033[33mO PC escolheu:\033[m {opções[o]}')  # Imprime a escolha da máquina
    print('\033[33m- RESULTADO:\033[m', end=' ')
    if jogador == pc:
        print('EMPATE!')
        print('-' * 50)
    else:  # Essa condição é iniciada quando a escolha do jogador é diferente da máquina
        if jogador == 0 and pc == 2:
            print('\033[32mBoa! Você venceu.')
            vitória += 1
        elif jogador == 1 and pc == 0:
            print(f'\033[32mParabéns, {nome}! Você venceu.')
            vitória += 1
        elif jogador == 2 and pc == 1:
            print(f'\033[32mMuito bem, {nome}!')
            vitória += 1
        elif jogador == 2 and pc == 0:
            print('\033[31mOps... Não foi dessa vez...')
            derrota += 1
        elif jogador == 0 and pc == 1:
            print('\033[31mVocê perdeu...')
            derrota += 1
        elif jogador == 1 and pc == 2:
            print('\033[31mBoa sorte na próxima vez.')
            derrota += 1
        print('\033[m=' * 50)
        print(f'\033[1;33m{" PLACAR ":-^50}\033[m\n\033[33m{"|PC:":>19} {derrota} x {nome}: {vitória}|\033[m')
        print('=' * 50)
    repetir = input('Quer repetir?[s/n] ').strip().lower()[0]
    while not repetir in 'SsNn':  # Esse loop é iniciado quando resposta for inválida
        repetir = input('Resposta inválida. Quer repetir?[s/n] ').strip().lower()[0]
    if repetir in 'Nn':
        print('SAINDO...')
        sleep(3)
        break
print('=-' * 25 + f'\033[1m\n{"FIM DE JOGO":>30}.\033[m')
