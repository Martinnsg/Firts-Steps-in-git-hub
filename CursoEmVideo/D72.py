#contamgem numerica por extenso
n = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    
    p = int(input('Digite um número de 0 a 20: '))

    if (0 <= p <= 20):
        print(f'{n[p]}')
        break
    else:
        print('Tente novamente')
   
