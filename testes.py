# tentando entender o enumerate com os dict:
# dict1= {'Nome': 'Matheus', 'Idade': 20}
# lista1= [dict1]
# print(dict1)
# print(lista1)
# print()


# dict2= {'Nome': 'Hian', 'Idade': 23}
# lista2= [dict1, dict2]
# print(dict2)
# print(lista2)
# print()
# # [{'Nome': 'Matheus', 'Idade': 20}, {'Nome': 'Hian', 'Idade': 23}]

# for indice, dicts in enumerate(lista2, start= 1):
#     print(f'INDICE:{indice}; DICONARIO: {dicts}' )

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# tentando excluir um contato:
dict1= {'Nome': 'Matheus', 'Idade': 20}
dict2= {'Nome': 'Hian', 'Idade': 23}

lista= [dict1, dict2]

for indice, dicts in enumerate(lista, start= 1):
    print(f'INDICE:{indice}; DICONARIO: {dicts}' )

selecionar= int(input('Escolha o íncidce: ')) -1
excluir= lista.pop(selecionar)
print(lista)