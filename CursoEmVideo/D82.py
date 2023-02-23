#crie um lista com varios numeros inseridos. depois divida essa lista em outras duas listas, uma par e uma impar
import os
lista = []
par = []
imp = []

while True:
    lista.append(int(input('Digite um valor: ')))
    n = str(input('Deseja adicionar outro número? [S/N]: ')).upper()
    if n == 'N':   
        break

for i,v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 ==1:
        imp.append(v)

print('='*30)
print(f'A lista digitada foi {lista}')
if len(par) == 0:
    print('Não há números pares nessa lista.')
else:
    print(f'Os números pares dessa lista são: {par}')

if len(imp) == 0:
    print('Não há números impares nessa lista.')
else:
    print(f'Os números impares dessa lista são: {imp}')    


        
        
           