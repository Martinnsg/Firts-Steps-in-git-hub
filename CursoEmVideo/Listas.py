#listas
#lista.append(item)
#lista.insert(0,item) --> insere o item na posição 0, não substitui nada
#del.lista[3] elimina item da posição 3
#lanche.pop(3) --> comando pop apaga o ultimo item da lista, mas da para colocar indice
#lanche.remove('item') --> comando remove vc nao indica o indice, indica o valor ou algo que quer eliminar
#if 'pizza' in lanche:
    #lanche.remove('pizza')
#valores = list(range(4,11)) --> vai criar uma lista em valores de 4 a 10
#valores.sort() --> ordena os valores
#valores.sort(reverse=True) --> ordena na ordem decrescente
#for i,v in enumerate(lista):

# pessoas = [['pedro',25],['Maria',19],['joao',20]]
# print(pessoas[0])

# teste = []
# galera = []
# teste.append('Gustavo')
# teste.append(40)
# print(teste[0])
# print(teste[1])
# galera.append(teste[:])
# print(galera)

galera = [['joao',19],['gabriel',20],['gustavo', 21],['leonardo',24]]
for p in galera:
    print(p)
    print(p[0])