# https://efficient-sloth-d85.notion.site/Desafio-01-622bb29769034c9ba659f2dc33019055#ac72d68b94f94627982db9f88583dd2b

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# funcão 1:
def adicionar_contato(nome, telefone, email):
    contato= {'Nome': nome, 'Telefone': telefone, 'E-Mail': email}
    contatos.append(contato)
    print('\n\n\n-> Contato adicionado com sucesso!')
    return

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# função 2:
def ver_contatos(contatos):
    print('\nLista de contatos:')
    for indice, contatos in enumerate(contatos, start= 1):
        print(f'-> {indice}º Contato -> {contatos}')
    return

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# função 3:
def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_ajustado= int(indice_contato) -1
    if indice_ajustado > 0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado] ['Nome']= novo_nome  
        contatos[indice_ajustado] ['Telefone']= novo_telefone
        contatos[indice_ajustado] ['E-Mail']= novo_email
        print(f'\n\n\n->Contato {indice_contato} atualizado com sucesso!')
    else:
        print('\n\n\nContato não encontrado...')
    return

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# função 4:
def apagar_contato(contatos, selecionar_excluir):
    if selecionar_excluir > 0 and selecionar_excluir < len(contatos):
        contatos.pop(selecionar_excluir)
        print(f'\n\n\n->Contato {selecionar_excluir + 1} apagado com sucesso!')
    else:
        print('\n\n\nContato não encontrado...')
    return

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

contatos= []
while True:
    print('\n---> Lista de contatos eletrônica <---')
    print('\n1 -> Adicionar um contato.')
    print('2 -> Vizualizar lista de contatos.')
    print('3 -> Editar um contato existente.')
    print('4 -> Apagar um contato existente.')
    print('5 -> Fechar o programa.')
    escolha= input('---> Digite um número para inciar a aplicação: ')

    if escolha == '1':
        print('\nPreencha os campos: ')
        nome= input(str('Nome: '))
        telefone= input(str('Telefone: '))
        email= input(str('E-Mail: '))
        adicionar_contato(nome, telefone, email)

    elif escolha == '2':
        print('\nLista de contatos:')
        ver_contatos(contatos)

    elif escolha == '3':
        ver_contatos(contatos)
        indice_contato= input('\n--->Digite o índice do contato que deseja atualizar: ')
        novo_nome= input('Edite o Nome : ')
        novo_telefone= input('Edite o Telefone : ')
        novo_email= input('Edite o E-Mail : ')
        editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)


    elif escolha == '4':
        ver_contatos(contatos)
        selecionar_excluir= int(input('\n--->Digite o índice do contato que deseja apagar: ')) -1
        apagar_contato(contatos, selecionar_excluir)

    elif escolha == '5':
        break
print('\n\n\nO programa foi encerrado...')
    

