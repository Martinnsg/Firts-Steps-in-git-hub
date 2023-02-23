#voto obrigatorio
def voto (ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'O voto com {idade} não é obrigatório.'
    elif 16<= idade <18 or idade>65:
        return f'O voto com {idade} é opcional.'
    else:
        return f'O voto com {idade} é obrigatório.'

nasc = int(input('Informe seu ano de nascimento: '))
print(voto(nasc))