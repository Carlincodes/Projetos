import os
import functions

while True:
  os.system('clear')
  print('''
=== Menu inicial ===

[1] Entrar
[2] Registrar Usuário
[3] Sair
''')
  opcao = int(input('Digite a opção desejada: '))

  if opcao == 1:
    while True:
      os.system('clear')
      print('''=== Login ===

Digite seu login (número de telefone) e senha, ou digite "exit" no lugar do login para voltar ao menu inicial: '''
            )
      login = input('\nLogin: ')
      senha = input('\nSenha: ')
      if login == 'exit':
        break
      elif functions.verif_login(login, senha) and functions.login_existe(
          login, senha):
        functions.menu_principal(login)
        break
      else:
        input(
          '\nLogin ou senha inválidos, pressione Enter para tentar novamente. '
        )

  elif opcao == 2:
    functions.registro()
  elif opcao == 3:
    break
  else:
    input(
      '\nOpção inválida! Digite apenas números (1,2 ou 3). Pressione Enter para tentar novamente. '
    )

print('\nPrograma encerrado!')
