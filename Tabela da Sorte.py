from random import randint as rd
from time import sleep
tabela = []
números = []

def Separador(separador):
    '''Apenas para fins de deixar mais organazido
    quando o conteúdo for mostrado no terminal'''
    print('-' * separador)

def Separador_2(separador):
    '''Apenas para fins de deixar mais organazido
    quando o conteúdo for mostrado no terminal'''
    print('=' * separador)

Separador_2(70)
print(f'<<{" TABELA DA SORTE ":-^66}>>')
partidas = 4
valor_atual = recompensa = total_arrecadado = total_n = 0
while True:  # Começa aqui
    Separador_2(70)
    print(f'Partidas: {partidas}')
    n = int(input('- Escolha seu número da sorte entre \033[4m0\033[m e \033[4m300\033[m: '))
    while n < 0 or n > 300:  # Entra nessa condição, caso o número digitado seja inválido
        n = int(input('\033[31mNúmero inválido! \033[mEscolha entre \033[4m0\033[m e \033[4m300\033[m: '))
    partidas -= 1  # Remove uma partida
    sleep(0.5)

    x_y = 14
    for x in range(0, x_y):  # Eixo X
        for y in range(0, x_y):  # Eixo Y
            tabela_valores = rd(0, 300)
            números.append(tabela_valores)
        tabela.append(números[:])
        números.clear()

    # Criando a tabela
    print(f'<<{33 * "=-"}>>')
    for ln in range(len(tabela)):  # Linhas
        for cl in range(len(tabela)):  # Colunas
            if n != tabela[ln][cl]:
                print(f'|\033[1;34m{tabela[ln][cl]:^3}\033[m', end='|')
            else:  # Entra nessa condição, caso o número escolhido pelo usuário esteja na tabela
                print(f'|\033[1;33m{n:^3}\033[m', end='|')
                total_n += 1
        print()
    print(f'<<{33 * "-="}>>')
    sleep(2)

    if total_n > 0:
        valor_atual += recompensa
        if total_n == 1:
            recompensa = 50
        elif total_n == 2:
            recompensa = 100
        elif total_n == 3:
            recompensa = 500
        elif total_n >= 4:
            recompensa = 1500
        total_arrecadado += recompensa
        print(f'\033[1;32mParabéns! Seu número da sorte apareceu {total_n}x.\n'
              f'De R${valor_atual:.2f} subiu para +R${recompensa:.2f} ↑\033[m')
    else:
        print('\033[31m- NENHUM NÚMERO ENCONTRADO. BOA SORTE NA PRÓXIMA! :(\033[m')
    Separador(70)

    # Finalizando
    if partidas == 0:
        print(f'- SUAS PARTIDAS ACABARAM.')
        break
    rept = input(f'Você ainda tem {partidas} partida(s). Deseja repetir?[s/n] ')[0].strip()
    while rept not in 'SsNn':  # Entra nesse loop se a resposta não for válida
        rept = input('\033[31mDigite uma resposta válida.\033[m Deseja repetir?[s/n] ')[0].strip()
    tabela.clear()  # Limpa toda a lista "tabela"
    total_n = 0
    if rept in 'Nn':
        print('- SAINDO...')
        break
sleep(2.5)

Separador_2(70)
print(f'\033[1;7;33m{"VALOR TOTAL ARRECADADO:":>40} R${total_arrecadado:<27.2f}\033[m')
Separador_2(70)