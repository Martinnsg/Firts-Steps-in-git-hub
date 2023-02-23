#função que calcula a area
def area(l,c):
    area = l*c
    print(f'A área de um terreno de {l}x{c} é de: {area}m².')
   
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
