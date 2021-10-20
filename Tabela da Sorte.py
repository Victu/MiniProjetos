from random import randint as rd
from time import sleep
tabela = []
números = []
print('=' * 70)
print(f'<<{" TABELA DA SORTE ":-^66}>>')
print('=' * 70)
recompensa = total_arrecadado = sorteado = total_n = 0
rodada = 3

while True:  # Início
    print(f'Rodadas: {rodada}')
    n = int(input('- Escolha seu número da sorte entre \033[4m0\033[m e \033[4m300\033[m: '))
    while n < 0 or n > 300:  # Entra nessa condição, caso o número digitado seja inválido
        n = int(input('\033[31mNúmero inválido! \033[mEscolha entre \033[4m0\033[m e \033[4m300\033[m: '))
    rodada -= 1

    y_x = 14
    for y in range(0, y_x):  # Eixo Y
        for x in range(0, y_x):  # Eixo X
            tabela_valores = rd(0, 300)
            números.append(tabela_valores)
        tabela.append(números[:])
        if n in números:
            sorteado = n
        números.clear()
    # Criando a tabela
    print(f'<<{33 * "=-"}>>')
    for cl in range(len(tabela)):  # Colunas
        for ln in range(len(tabela)):  # Linhas
            if sorteado != tabela[cl][ln]:
                print(f'|\033[1;34m{tabela[cl][ln]:^3}\033[m', end='|')
            else:  # Entra nessa condição, caso o número escolhido pelo usuário esteja na tabela
                print(f'|\033[1;33m{sorteado:^3}\033[m', end='|')
                total_n += 1
        print()
    print(f'<<{33 * "-="}>>')
    sleep(2)

    recebido = recompensa
    if total_n == 1:
        recompensa = 50
    elif total_n == 2:
        recompensa = 100
    elif total_n >= 3:
        recompensa = 500
    print(f'\033[1;32mParabéns! Seu número da sorte foi encontrado {total_n}x!\n'
          f'De R${recebido:.2f} subiu para +R${recompensa:.2f} ↑\033[m'
          if total_n > 0 else '\033[31m- NENHUM NÚMERO SORTEADO. BOA SORTE NA PRÓXIMA! :(\033[m')
    total_arrecadado += recompensa

    # Finalizando
    if rodada == 0:
        print(f'- RODADAS TERMINADA.')
        print('=' * 70)
        break
    rept = input(f'Você ainda tem {rodada} rodada(s). Deseja repetir?[s/n] ')[0].strip()
    while rept not in 'SsNn':
        rept = input('\033[31mDigite uma resposta válida.\033[m Deseja repetir?[s/n] ')[0].strip()
    tabela.clear()
    total_n = 0
    print('=' * 70)
    if rept in 'Nn':
        break
sleep(2.5)
print(f'\033[1;7;33m {"VALOR TOTAL ARRECADADO:":>40} R${total_arrecadado:.2f}\t\t   '
      f'           \033[m')
print('=' * 70)