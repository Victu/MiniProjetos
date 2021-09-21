from time import sleep
from emoji import emojize as emj
from datetime import time, datetime
from random import randint

def Regra():
    pass

# Função que calcula o total das respectivas cédulas/notas usadas
def TotalCédulas(valor_saque):
    montante = valor_saque
    cédula = 100
    total_cédulas = 0
    while not montante == 0:
        montante -= cédula
        total_cédulas += 1
        if montante < cédula:
            if total_cédulas > 0:
                print(f'Total de {total_cédulas} cédula(s)'
                      f' de R${cédula},00 utilizada(s).')
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
    print(emj(f'{" TELA DE CADASTRO ":>66} ', use_aliases=True))
    print(f'{"=" * 100:>110}')
    print(f'{"Crie uma conta para poder ter acesso ao caixa eletrônico virtual":>92}')

    print(f'{">>" + "-" * 80:>100}<<')
    print(emj(f'{":rotating_light: ATENÇÃO!":>75}', use_aliases=True))
    print(f'{"1) Nome de usuário não pode ser igual seu nome, não pode estar vazio e":>92}\n'
          f'{"nem ser numérico":>41}.')
    print(f'{"2) Senha não pode ficar vazia e nem conter caracteres de caixa alta.":>90}')
    print(f'{"3) Nome de usuário tem que ter pelo menos 3 digitos, e senha pelo menos 4.":>96}')
    print(f'{"4) O horário de funcionamento é até às 22hr.":>66}')
    print(f'{">>" + "-" * 80:>100}<<')

    print('Primeiramente, informe alguns dados.')  # Informações básicas
    name = input('Nome: ').lstrip()
    sx = input('Sexo [M/F]: ').strip().lower()[0]
    while not sx in 'FfMm':
        sx = input('Dado inválido. Tente novamente. Sexo [M/F]: ')

        # Criando um nome de usuário.
    new_user = input('Crie um nome de usuário: ').lstrip()
    if new_user.isnumeric() or new_user.isspace() or len(new_user) <= 2 or new_user == name:  # Entra nessa condição
        while True:  # Se o nome de usuário for inválido
            new_user = input('Crie um nome de usuário válido: ')
            if not new_user.isnumeric() and not new_user.isspace() and len(new_user) > 2 and new_user != name:
                break
                # Criando uma senha.
    new_password = input('Crie uma senha: ').strip()
    if new_password.isspace() or new_password.isupper() or len(
            new_password) <= 3:  # Entra nesse loop infinito caso a senha esteja inválida.
        print('Esta senha não é válida.')
        while True:
            new_password = input('Tente novamente. Crie outra senha: ')
            if not new_password.isupper() and not new_password.isspace() and len(new_password) > 3:
                break
    name = name.title()
    # Conclusão do cadastro
    print('==' * 49)
    print('Concluindo cadastro', end=" ")
    N = 0
    while N < 11:
        print(emj(':white_small_square:' * N, use_aliases=True), end="" if N < 10 else ' Concluido com sucesso!\n')
        N += 1
        sleep(0.4)
    print(emj(f'{"Cadastro realizado em":>46} {data_hora} :clock1030:', use_aliases=True))
    print('==' * 49)
    print('Você será direcionado para a seção de Login...')
    sleep(3.5)
    for espaços in range(0, 33):
        print('')

        # Tela de Login para acessar o caixa eletrônico virtual
    if sx in 'Ff':
        print("==" * 55)
        print(emj(f'{"":>41}:woman: Seja bem vinda, {name}! :woman:', use_aliases=True))
        print("==" * 55)
    elif sx in 'Mm':
        print("==" * 55)
        print(emj(f'{"":>41}:man: Seja bem vindo, {name}! :man:', use_aliases=True))
        print("==" * 55)
    for espaços in range(0, 4):
        print('')

    user = input(emj(':bust_in_silhouette: Informe seu nome de usuário: ', use_aliases=True))
    print('Verificando se há problemas...')
    sleep(1)
    while user.isnumeric() or user != new_user:
        print('-' * 50)
        user = input('Nome de usuário incorreto.'
                     ' Tente novamente: ')
        print('Varificando se há algum problema...')
        sleep(1.5)
    print(emj(f'     :arrow_forward: Tudo OK! :arrow_backward:', use_aliases=True))

    password = input(emj(':lock: Digite sua senha: ', use_aliases=True))
    print('Verificando se há problemas...')
    sleep(2)
    while password.isspace() or password.isupper() or password != new_password:
        print('-' * 50)
        password = input('Senha inválida. '
                         'Insira a senha novamente: ')
        print('Verificando se há algum problema...')
        sleep(2)
    print(emj('     :arrow_forward: Tudo OK! :arrow_backward:', use_aliases=True))

    # Finalizando Login
    print('==' * 38)
    print('Efetuando Login', end=" ")
    N = 0
    while N < 11:
        print(emj(':black_small_square:' * N, use_aliases=True), end="" if N < 10 else ' 100%\n')
        N += 1
        sleep(0.4)
    print('==' * 38)
    print('Acessando caixa eletrônico virtual...')
    sleep(3)
    for espaços in range(0, 33):
        print('')

        # Caixa eletrônico virtual
    print("==" * 55)
    print(emj(f'{" :moneybag: :bank: CAIXA ELETRÔNICO VIRTUAL":>79} :bank: :moneybag:', use_aliases=True))
    print("==" * 55)
    cent = randint(10, 99)
    saldo_disponível = randint(100, 12500)
    notas = ('R$100,00', 'R$50,00', 'R$20,00',
             'R$10,00', 'R$5,00', 'R$1,00')

    print(f'{"Usuário:":>55} {user}')
    print(f'Acessado hoje às {hora_funcionamento:<29} {"Nome:"} {name}')
    print('=-' * 55)
    print(f'{"Saldo disponível:":>56} R${saldo_disponível},{cent}')
    print(f'{"AVISO: O valor mínimo permitido para saque é 100 reais":>80}')
    print('==' * 55)
    print('- CÉDULAS DISPONÍVEIS:')
    for x in notas:
        print(emj(f':dollar: {x}', use_aliases=True))

    resposta = ''
    while True:
        saque = int(input('- Informe o valor que deseja sacar: R$'))  # Entra neste loop para informar o valor do saque
        while saque < 100 or saque > saldo_disponível:
            if saque < 100:
                print('No momento, o mínimo permitido para saque é 100 reais.')
            if saque > saldo_disponível:
                print(f'{name}, você escolheu um valor acima dos R${saldo_disponível},{cent} disponível.')
            saque = int(input('- Escolha outro valor: R$'))
            print('Verificando se há problemas...')
            sleep(2)
            if saque >= 100:
                if saque <= saldo_disponível:
                    print('Nenhum problema encontrado.', end=' ')
                    break
        print('Aguarde enquanto faz a contagem das notas...')
        sleep(3.5)
        print('-' * 50)
        TotalCédulas(valor_saque=saque)
        saldo_disponível -= saque

        if 0 <= saldo_disponível < 100:
            print(f'SALDO RESTANTE: R${saldo_disponível},{cent}\nSTATUS: Saldo insuficiente para saque.')
            print('-' * 50)
            break
        elif saldo_disponível >= 100:
            print(f'SALDO RESTANTE: R${saldo_disponível},{cent}')
            print('-' * 50)
            resposta = input('Deseja realizar outro saque[S/N]? ').strip().upper()[0]
            while not resposta in 'NnSs':
                resposta = input('Responda somente com "sim" ou "não": ').strip().upper()[0]

        if resposta in 'Nn':
            print('-' * 50)
            print(f'STATUS: {name}, você ainda tem saldo disponível em sua conta.' if saldo_disponível > 100
                  else 'SITUAÇÃO: Saldo insuficiente para saque.')
            print('-' * 50)
            break
    print('Finalizando...')
    sleep(4)
    print('=' * 50 + '\n      FINALIZADO COM SUCESSO. VOLTE SEMPRE!')  # Fim
else:  # Entra nessa condição quando chega o horário das 22hr
    print('<<' * 48)
    print(emj(f'{"    :construction: SISTEMA INDISPONÍVEL NO MOMENTO. RETORNE AMANHÃ. :construction:":>95}',
              use_aliases=True))
    print('>>' * 48)
