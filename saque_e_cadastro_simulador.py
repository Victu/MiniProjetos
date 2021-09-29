from time import sleep
from emoji import emojize as emj
from datetime import time, datetime
from random import randint

def Regra():
    pass

def TotalCédulas(valor_saque):
    """Função que calcula o total das
    respectivas cédulas/notas usadas na contagem"""
    montante = valor_saque
    cédula = 100
    total_cédulas = 0
    while not montante == 0:
        montante -= cédula
        total_cédulas += 1
        if montante < cédula:
            if total_cédulas > 0:
                print(f'\033[32mNotas de \033[1mR${cédula},00\033[m \033[32mutilizadas:\033[m '  # Imprime o total das notas utilizadas
                      f'\033[31m-{total_cédulas}\033[m \033[32mnota(s)\033[m')
                sleep(1)
                total_cédulas = 0
            cédula = 50
        if montante < cédula:
            cédula = 20
        if montante < cédula:
            cédula = 10
        if montante < cédula:
            cédula = 5
        if montante < cédula:
            cédula = 1

data_hora = datetime.today().strftime(emj(':date: %d/%m/%Y às %H:%M'))  # Data no formato padrão brasileiro
hora_funcionamento = datetime.today().strftime('%H:%M:%S')
hora_fechamento = time().strftime('22:00:00')

if hora_fechamento > hora_funcionamento:  # Início
    print(f'{"=" * 100:>110}')
    print(emj(f'\033[1m{" TELA DE CADASTRO ":>66}\033[m ', use_aliases=True))
    print(f'{"=" * 100:>110}')
    print(f'\033[1m{"Crie uma conta para poder ter acesso ao caixa eletrônico virtual":>92}\033[m')

    print(f'{">>" + "-" * 80:>100}<<')
    print(emj(f'\033[31m{":rotating_light:":>68} \033[1mATENÇÃO!\033[m', use_aliases=True))
    print(f'\033[31m{"1) Nome de usuário não pode ser igual seu nome, não pode estar vazio e":>92}\n'
          f'{"nem ser numérico":>41}.')
    print(f'{"2) Senha não pode ficar vazia e nem conter caracteres de caixa alta.":>90}')
    print(f'{"3) Nome de usuário tem que ter pelo menos 3 digitos, e senha pelo menos 4.":>96}')
    print(f'{"4) O horário de funcionamento é até às 22hr.":>66}\033[m')
    print(f'{">>" + "-" * 80:>100}<<')

    print('\033[1mPreencha os campos abaixo:\033[m')  # Informações básicas
    name = input('Nome: ').lstrip()
    sx = input('Sexo [M/F]: ').strip().lower()[0]
    while not sx in 'FfMm':
        sx = input('\033[31mDado inválido. Tente novamente. Sexo [M/F]: \033[m').strip().lower()[0]

    # Criando um nome de usuário
    new_user = input('Crie um nome de usuário: ').lstrip()
    if new_user.isnumeric() or new_user.isspace() or len(new_user) <= 2 or new_user == name:  # Entra nessa condição
        while True:  # Se o nome de usuário for inválido
            new_user = input('\033[31mCrie um nome de usuário válido: \033[m')
            if not new_user.isnumeric() and not new_user.isspace() and len(new_user) > 2 and new_user != name:
                break
    # Criando uma senha
    new_password = input('Crie uma senha: ').strip()
    if new_password.isspace() or new_password.isupper() or len(new_password) <= 3:  # Entra nesse loop infinito caso a senha esteja inválida.
        while True:
            new_password = input('\033[31mEsta senha não é válida!\nTente novamente. Crie outra senha: \033[m')
            if not new_password.isupper() and not new_password.isspace() and len(new_password) > 3:
                break
    name = name.title()
    # Conclusão do cadastro
    print('==' * 49)
    print('\033[36mConcluindo cadastro\033[m', end=" ")
    N = 0
    while N < 11:
        print(emj('\033[36m:black_small_square:\033[m' * N, use_aliases=True), end="" if N < 10 else ' \033[34mConcluido com sucesso!\033[m\n')
        N += 1
        sleep(0.4)
    print(emj(f'\033[36m{"Cadastro realizado em":>46} {data_hora} :clock1030:\033[m', use_aliases=True))
    print('==' * 49)
    print('Você será direcionado para a seção de Login...')
    sleep(3.5)
    for espaços in range(0, 33):  # Apenas alguns espaços vazios adicionados
        print('')

    # Tela de Login para acessar o caixa eletrônico virtual
    if sx in 'Ff':
        print('==' * 55)
        print(emj(f'\033[35m{"":>41}:woman: Seja bem vinda, {name}! :woman:\033[m', use_aliases=True))
        print('==' * 55)
    elif sx in 'Mm':
        print('==' * 55)
        print(emj(f'\033[34m{"":>41}:man: Seja bem vindo, {name}! :man:\033[m', use_aliases=True))
        print('==' * 55)
    for espaços in range(0, 4):
        print('')

    print('\033[1;4m- INFORME SEUS DADOS\033[m')
    user = input(emj(':bust_in_silhouette: Seu nome de usuário: ', use_aliases=True))
    print('Verificando se há problemas...')
    sleep(1)
    while user.isnumeric() or user != new_user:
        print('-' * 50)
        user = input('\033[31mNome de usuário incorreto.'
                     ' Tente novamente: \033[m')
        print('Varificando se há algum problema...')
        sleep(1.5)
    print(emj(f'\033[32m     :arrow_forward: Tudo OK! :arrow_backward:\033[m', use_aliases=True))

    password = input(emj(':lock: Digite sua senha: ', use_aliases=True))
    print('Verificando se há problemas...')
    sleep(2)
    while password.isspace() or password.isupper() or password != new_password:
        print('-' * 50)
        password = input('\033[31mSenha inválida. '
                         'Insira a senha novamente: \033[m')
        print('Verificando se há algum problema...')
        sleep(2)
    print(emj('\033[32m     :arrow_forward: Tudo OK! :arrow_backward:\033[m', use_aliases=True))

    # Finalizando Login
    print('==' * 38)
    print('Efetuando Login', end=" ")
    N = 0
    while N < 11:
        print('\033[37;47m \033[m' * N, end="" if N < 10 else ' \033[32m100%\033[m\n')
        N += 1
        sleep(0.4)
    print('==' * 38)
    print('Acessando caixa eletrônico virtual...')
    sleep(3)
    for espaços in range(0, 33):
        print('')

    # Iniciando caixa eletrônico virtual
    print("\033[32m==" * 55 + '\033[m')
    print(emj(f'\033[33m{" :moneybag: :bank: CAIXA ELETRÔNICO VIRTUAL":>79} :bank: :moneybag:\033[m', use_aliases=True))
    print("\033[32m==" * 55 + '\033[m')
    cent = randint(10, 99)
    saldo_disponível = randint(100, 20500)
    notas = ('R$100,00', 'R$50,00', 'R$20,00',  # Todas as notas disponíveis
             'R$10,00', 'R$5,00', 'R$1,00')

    print(f'\033[33m{"Usuário:":>55} {user}')
    print(f'Acessado hoje às {hora_funcionamento:<29} {"Nome:"} {name}\033[m')
    print('=-' * 55)
    print(f'\033[1;33m{"Saldo disponível:":>56} R${saldo_disponível},{cent}\033[m')
    print(f'\033[31m{"AVISO: O valor mínimo permitido para saque é 100 reais":>80}\033[m')
    print('==' * 55)
    print('- NOTAS DISPONÍVEIS:')
    for x in notas:
        print(emj(f'\033[32m:dollar: {x}\033[m', use_aliases=True))

    resposta = ''
    while True:
        saque = int(input('- Informe o valor que deseja sacar: R$'))  # Entra neste loop para informar o valor do saque
        while saque < 100 or saque > saldo_disponível:
            if saque < 100:
                print('\033[31mNo momento, o mínimo permitido para saque é 100 reais.\033[m')
            if saque > saldo_disponível:
                print(f'\033[31m{name}, você escolheu um valor acima dos R${saldo_disponível},{cent} disponível.\033[m')
            saque = int(input('\033[31m- Escolha outro valor: R$\033[m'))
            print('Verificando se há problemas...')
            sleep(2)
            if saque >= 100:
                if saque <= saldo_disponível:
                    print('\033[32mNenhum problema encontrado.', end=' ')
                    break
        print('Aguarde enquanto faz a contagem das notas...\033[m')
        sleep(3.5)
        print('-' * 50)
        TotalCédulas(valor_saque=saque)
        saldo_disponível -= saque

        if 0 <= saldo_disponível < 100:
            print(f'\033[1;33m- SALDO RESTANTE: R${saldo_disponível},{cent}\033[m\n\033[31mSTATUS: Saldo insuficiente para saque.\033[m')
            print('-' * 50)
            break
        elif saldo_disponível >= 100:
            print(f'\033[1;33m- SALDO RESTANTE: R${saldo_disponível},{cent}\033[m')
            print('-' * 50)
            resposta = input('Deseja realizar outro saque[S/N]? ').strip().upper()[0]
            while not resposta in 'NnSs':
                resposta = input('\033[31mResponda somente com "sim" ou "não": \033[m').strip().upper()[0]

        if resposta in 'Nn':
            print('-' * 50)
            print(f'\033[36mSTATUS: {name}, você ainda tem saldo suficiente para saque.\033[m' if saldo_disponível > 100
                  else '\033[31mSTATUS: Saldo insuficiente para saque.\033[m')
            print('-' * 50)
            break
    print('- Finalizando...')
    sleep(4)
    print('=' * 50 + '\n      FINALIZADO COM SUCESSO. VOLTE SEMPRE!')  # Fim
else:  # Entra nessa condição quando chega o horário das 22hr
    print('\033[31m<<' * 48)
    print(emj(f'{"    :construction: SISTEMA INDISPONÍVEL NO MOMENTO. RETORNE AMANHÃ. :construction:":>95}',
              use_aliases=True))
    print('>>' * 48 + '\033[m')
