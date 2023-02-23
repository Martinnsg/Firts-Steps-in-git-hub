#cadastro de trabalhador
from datetime import datetime
import os
trabalhador = dict()
trabalhador['nome'] = str(input('Informe seu nome: '))
nasc = int(input('Qual seu ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['CTPS'] = int(input('CTPS (0 não tem): '))
if trabalhador['CTPS'] == 0:
    print('Você nao tem ctps')
else:
    trabalhador['contratação'] = int(input('Informe o ano de contrtação: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador["contratação"] + 35) - datetime.now().year)
    trabalhador['sal'] = float(input('Informe seu salário: '))
    os.system('cls')
    print(f'Nome: {trabalhador["nome"]}')
    print(f'Idade: {trabalhador["idade"]}')
    print(f'CTPS: {trabalhador["CTPS"]}')
    print(f'Irá aposentar com: {trabalhador["aposentadoria"]} anos.')
    print(f'Salário: {trabalhador["sal"]}')
    