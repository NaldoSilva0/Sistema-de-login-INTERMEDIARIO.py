import os

if not os.path.exists('LogEntrada.txt'):
    with open('LogEntrada.txt', 'w', encoding='utf-8') as log:
        log.write('\n---CADASTRO DE USUARIOS---\n')

def usuarioReg(usuario, senha):
    with open('LogEntrada.txt','a', encoding='utf-8') as log:
        log.write(f'{usuario};{senha}\n')

def listaReg():
    print('[1]-REGISTRAR CONTA')
    print('[2]-LOGAR CONTA')
    print('[3]-SAIR')
    resposta = input('Digite sua opção: ')
    return resposta

def listaPlogin():
    print('[1]-ALTERAR SENHA')
    print('[2]-INFORMAÇÔES DA CONTA')
    print('[3]-LOGOUT')
    resposta = input('Digite a opção: ')
    return resposta

def mudarSenha(nomeAlvo, novaSenha):
    with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
        linhas = log.readlines()

    with open('LogEntrada.txt', 'w', encoding='utf-8') as log:
        for linha in linhas:
            if ';' in linha:
                usuarioRegistro, senhaRegistro = linha.strip().split(';')
                if usuario == nomeAlvo:
                    log.write(f'{usuario};{novaSenha}\n')
                else:
                    log.write(linha)
            else:
                log.write(linha)



with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
    linhas = log.readlines()

respostaLista = listaReg()
contaExiste = False

while True:
    if respostaLista == '1':
        print('Menu de registro\n')
        print('-=-'*20)
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        repSenha = input('Repita a senha: ')
        print('-=-'*20)
        respostaLista = listaReg()
        usuarioReg(usuario, senha)
        
    
        if repSenha != senha:
            print('As senhas não são compátiveis, tente novamente!!')
            senha = input('Senha: ')
            repSenha = input('Repita a senha: ')
            print('-=-'*20)

    elif respostaLista == '2': 
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        print('-=-'*20)
        with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
            linhas = log.readlines()
        
        contaExiste = False
        
        for linha in linhas:
            if ';' in linha:
                usuarioRegistro, senhaRegistro = linha.strip().split(';')

                if usuario == usuarioRegistro and senha == senhaRegistro:
                    contaExiste = True
                    break
        
        if contaExiste:
            loginCompleto = print('Login Completo!!')
            break
        else:
            print('Informações incorretas!!')

    elif respostaLista == '3': 
        print('Obrigado por usar nossos serviços!!')
        break
    else:
        print('Opção inválida\n')

from datetime import date, datetime

data = date.today()
hora = datetime.now().strftime('%H:%M:%S')

if not os.path.exists('LogLogout.txt'):
    with open('LogLogout.txt', 'w', encoding='utf-8') as regLL:
        print('---INÍCIO DE LOG---')

    with open('LogLogout.txt', 'a', encoding='utf-8') as regLL:
        regLL.write(f'{usuario} Logou - {data} - {hora}\n')

menuConfig = listaPlogin()

contador = 5

while True:
    if menuConfig == '1':
        confirmarSenha = input('Digite a senha atual: ')
        print('-=-'*20)
        if confirmarSenha != senha:
            contador -= 1
            print('A senha digitada não é igual a atual, tente novamente.')
            print(f'Restam {contador} antes de bloquearmos as tentativas pela segurança de sua conta.')
        else:
            senhaNova = input('Digite a nova senha: ')
            repSenhaNova = input('Digite a nova senha novamente: ')
            if repSenhaNova != senhaNova:
                print('As senhas não são iguais, tente novamente')
                senhaNova = input('Digite a nova senha: ')
                repSenhaNova = input('Digite a nova senha novamente: ')
            else:
                print('Senha trocada com sucesso!!')
                print('-=-'*20)
                newSenha = mudarSenha(usuario, senhaNova)
                break
    
    elif menuConfig == '2':
        print('---INFORMAÇÔES DA CONTA---\n')
        print('-=-'*20)

        print(f'Você logou na conta: {usuario}')
        print(f'Você logou na conta pela ultima vez em: {data} - {hora}')
        print('-=-'*20)
        voltaMenu = input('Deseja voltar para o menu das configurações?[S/N] ').lower()
        if voltaMenu == 's':
            menuConfig = listaPlogin()
        else:
            break

    elif menuConfig == '3':
        confirmar = input('Tem certeza que deseja dar logout da conta? [S/N] ').lower()
        if confirmar == 's':
            print('Obrigado por usar nossos serviços!!')
            print('-=-'*20)
            respostaLista = listaReg()
            break
        elif confirmar == 'n':
            print('Então continue aproveitando nossos serviços!!')
            menuConfig = listaPlogin()
        else:
            print('Essa função não existe!!')
        
dataLogout = date.today()             
horaLogout = datetime.now().strftime('%H:%M:%S')
with open('LogLogout.txt', 'a', encoding='utf-8') as regLL:
    regLL.write(f'{usuario} Logout - {dataLogout} - {horaLogout}\n')

  


        