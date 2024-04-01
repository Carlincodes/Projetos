import os


def verif_login(login, senha):
  if login.isnumeric() and len(login) == 11 and senha.isalnum() and len(
      senha) == 6:
    return True
  else:
    return False


def registro():
  'Efetua o registro do usuário na lista de logins, caso já não exita uma conta criada'

  while True:
    os.system('clear')
    print('''
  === Registro ===

  No login, coloque seu telefone, com o DDD e o 9. totalizando 11 dígitos numéricos. A senha deve conter somente 6 caracteres, e deve ser composta de letras e números'''
          )
    login = input('\nLogin: ')
    senha = input('Senha: ')

    if login == 'exit':
      return

    elif verif_login(login, senha) and not login_existe(login, senha):
      arq = open('logins.txt', 'a')
      arq.write(f'{login} {senha}\n')
      arq.close()
      input(
        '\nCadastro criado com sucesso! Pressione Enter para voltar ao menu inicial. '
      )
      return

    elif login_existe(login, senha):
      input('\nEste login já existe. Pressione Enter para tentar novamente')

    elif not verif_login(login, senha):
      input(
        '\nLogin, ou senha invalido. Pressione Enter para tentar novamente. ')


def login_existe(login, senha):
  'Verifica se o número de telefone e a senha já existem na lista de logins, retornando "Falso" caso não exista'
  arq = open('logins.txt', 'r')
  for linha in arq:
    lista = linha.split()
    if len(lista) > 0:
      if lista[0] == login and lista[1] == senha:
        return True
  arq.close()
  return False


def menu_principal(login):
  'Menu que permite ao usuário acessar e modificar sua lista de contatos'
  while True:
    os.system('clear')
    print('''

=== Menu principal ===

[1] Adicionar Contato
[2] Listar Contatos
[3] Pesquisar Contato
[4] Remover Contato
[5] Alterar Contato
[6] Excluir Conta do Usuário
[7] Sair
''')
    option = int(input('Digite a opção desejada: '))
    if option == 1:
      add_cont(login)
    elif option == 2:
      listar_cont(login)
    elif option == 3:
      pesquisar_cont(login)
    elif option == 4:
      remover_cont(login)
    elif option == 5:
      alterar_cont(login)
    elif option == 6:
      excluir = excluir_conta(login)
      input(excluir)
      if excluir == 's':
        break
    elif option == 7:
      os.system('clear')
      print('Sessão encerrada!\n')
      input('Pressione Enter para retornar ao menu inicial. ')
      break
    else:
      input('\nOpção incorreta. Pressione Enter para tentar novamente. ')


def agenda_existe(login):
  'Verifica se existe uma agenda criada com o login do usuário e retorna True caso exista'

  arquivos = os.listdir('agendas')
  for arquivo in arquivos:
    if arquivo == login + '.txt':
      return True
  return False


def add_cont(login):
  'Adiciona um novo contato à conta do usuário'

  while True:
    os.system('clear')
    print('''
  === Adicionar contato ===

  Digite o nome e o telefone da contato que você quer adicionar. ''')
    nome = input('\nNome: ')
    telefone = input('\nTelefone: ')

    if telefone.isnumeric() and len(telefone) == 11:
      arq = open(f'agendas/{login}.txt', 'a')
      arq.write(f'{nome}&{telefone}\n')
      arq.close()
      return
    else:
      os.system('clear')
      input(
        '\nNúmero de telefone inválido. Ele deve ter 11 dígitos númericos (incluir ddd e o 9). Pressione Enter para tentar novamente. '
      )


def listar_cont(login):
  'Lista os contatos do usuário e retorna ao menu principal'

  if agenda_existe(login):
    os.system('clear')
    print('''=== Contatos ===
    ''')
    arq = open(f'agendas/{login}.txt', 'r')
    while True:
      linha = arq.readline()
      list_linha = linha.split('&')
      if len(list_linha) == 2:
        print(f' {list_linha[0]} - {list_linha[1]}')
      if linha == '':
        arq.close()
        input('\nPressione Enter para voltar ao menu principal. ')
        return
  else:
    os.system('clear')
    input(
      'Agenda inexistente. Adicione pelo menos um contato para criar sua agenda. Pressione Enter para voltar ao menu principal. '
    )


def pesquisar_cont(login):
  'Busca um contato específico dentro da agenda do usuário'

  if agenda_existe(login):
    os.system('clear')
    print('''=== Pesquisar contato ===
    
    Digite um nome para ser buscado na sua lista de contatos.
    ''')
    nome = input('Pesquisar: ').lower()
    arq = open(f'agendas/{login}.txt', 'r')
    cont = 0
    for linha in arq:
      linha_minuscula = linha.lower()
      if linha_minuscula.count(nome) > 0:
        os.system('clear')
        print('''Resultado: 
        ''')
        cont += 1
        list_linha = linha.split('&')
        print(f' {list_linha[0]} - {list_linha[1]}')
    arq.close()
    if cont > 0:
      input('\nPressione Enter para voltar ao menu principal. ')
    elif cont == 0:
      input(
        '\nNenhum contato encontrado. Pressione Enter para voltar ao menu principal'
      )

  else:
    os.system('clear')
    input(
      'Agenda inexistente. Adicione pelo menos um contato para criar sua agenda. Pressione Enter para voltar ao menu principal. '
    )


def remover_cont(login):
  'Remove um contato específico dentro da agenda do usuário'

  if agenda_existe(login):
    os.system('clear')
    print('''=== Remover contato ===
    
    Digite o nome de um contato para ser removido.
    ''')
    nome = input('Nome: ').lower()
    arq = open(f'agendas/{login}.txt', 'r')
    copia = open(f'agendas/copia_{login}.txt', 'w')
    contato_existe = 0
    for linha in arq:
      list_linha = linha.split('&')
      contato = list_linha[0].lower()
      if contato != nome:
        copia.write(linha)
      if contato == nome:
        contato_existe += 1
    arq.close()
    copia.close()
    os.remove(f'agendas/{login}.txt')
    os.rename(f'agendas/copia_{login}.txt', f'agendas/{login}.txt')

    if contato_existe > 0:
      input(
        '\nContato removido. Pressione Enter para retornar ao menu principal. '
      )
      return
    elif contato_existe == 0:
      input(
        '\nContato inexistente. Pressione Enter para voltar ao menú principal. '
      )
      return
  else:
    os.system('clear')
    input(
      'Agenda inexistente. Adicione pelo menos um contato para criar sua agenda. Pressione Enter para voltar ao menu principal. '
    )


def alterar_cont(login):

  while True:
    os.system('clear')
    print('''=== Alterar contato === 
  
    Digite um contato para alterar o numero de telefone
    ''')
    contato = input('Contato: ')
    novo_numero = input('Novo número: ')
    senha = 'abc123'
    if verif_login(novo_numero, senha):
      arq_original = open(f'agendas/{login}.txt', 'r')
      copia = open(f'agendas/copia_{login}.txt', 'w')
      cont = 0
      for linha in arq_original:
        list_cont = linha.split('&')
        if list_cont[0] == contato:
          cont += 1
          copia.write(f'{contato}&{novo_numero}\n')
        else:
          copia.write(linha)
      arq_original.close()
      copia.close()
      os.remove(f'agendas/{login}.txt')
      os.rename(f'agendas/copia_{login}.txt', f'agendas/{login}.txt')
      if cont == 0:
        os.system('clear')
        input(
          'Contato não encontrado! Pressione Enter para voltar ao menu principal'
        )
        return
      if cont == 1:
        os.system('clear')
        input(
          'O número de telefone do contato foi alterado com êxito. Pressione Enter para voltar ao menu principal. '
        )
        return
    else:
      input(
        'Numero de telefone inválido. Certifique-se que ele tenha 11 dígitos numéricos (incluindo ddd e 9). Pressione Enter para tentar novamente'
      )


def excluir_conta(login):
  os.system('clear')
  print('''=== Excluir conta ===
  
  Deseja mesmo remover sua conta e toda a sua agenda de contatos? (digite "s" para sim, ou "n" para não) 
  ''')
  while True:
    resposta = input('Resposta: ').lower()
    if resposta == 's':
      if agenda_existe(login):
        agenda = f'agendas/{login}.txt'
        os.remove(agenda)
      arq = open('logins.txt', 'r')
      copia = open(f'copia_logins.txt', 'w')
      for linha in arq:
        lista_linha = linha.split()
        if len(lista_linha) != 0:
          if lista_linha[0] != login:
            copia.write(linha)
      arq.close()
      copia.close()
      os.remove('logins.txt')
      os.rename('copia_logins.txt', 'logins.txt')
      print('Conta de usuário removida!')
      input('\nPressione Enter para voltar ao menu inicial ')
      return 's'
    elif resposta == 'n':
      return 'n'
    else:
      os.system('clear')
      input('Opção incorreta! Pressione Enter para tentar novamente. ')
