

---

# Sistema de Registro e Login em Python

Este projeto é um **sistema básico de gerenciamento de usuários** escrito em Python. Ele permite registrar usuários, realizar login, alterar senhas, visualizar informações da conta e registrar logs de login e logout.

---

## Funcionalidades

1. **Registro de Usuário**

   * Permite criar uma conta com nome de usuário e senha.
   * Verifica se as senhas digitadas coincidem antes de registrar.

2. **Login de Usuário**

   * Permite entrar em uma conta existente informando o usuário e a senha.
   * Valida as credenciais com os registros armazenados no arquivo `LogEntrada.txt`.

3. **Menu de Configuração Pós-Login**

   * Alterar senha: Permite atualizar a senha da conta.
   * Informações da conta: Exibe o nome do usuário e o horário do login.
   * Logout: Permite sair da conta e registrar a ação.

4. **Registro de Logs**

   * Cada login e logout é registrado no arquivo `LogLogout.txt` com data e hora.

---

## Estrutura de Arquivos

* **LogEntrada.txt**
  Armazena os usuários e senhas no formato:

  ```
  usuario;senha
  ```

* **LogLogout.txt**
  Armazena os registros de login e logout no formato:

  ```
  usuario Logou - YYYY-MM-DD - HH:MM:SS
  usuario Logout - YYYY-MM-DD - HH:MM:SS
  ```

---

## Como Usar

1. Execute o script Python.
2. No menu principal, escolha entre:

   * `[1]` Registrar Conta
   * `[2]` Logar Conta
   * `[3]` Sair
3. Após logar, será exibido o menu de configurações:

   * `[1]` Alterar Senha
   * `[2]` Informações da Conta
   * `[3]` Logout
4. Todas as alterações e logins/logouts serão registrados nos arquivos de log.

---

## Observações

* Senhas não são criptografadas (para uso em produção, utilize hash como bcrypt).
* O sistema não possui limite de usuários, mas cada registro é salvo em `LogEntrada.txt`.
* Ao alterar a senha, o arquivo de log é atualizado para refletir a nova senha.
* O contador de tentativas de alteração de senha bloqueia após 5 erros consecutivos.

---

## Dependências

* Python 3.x
* Módulos nativos: `os`, `datetime`

---

## Melhorias Futuras

* Implementar criptografia de senha.
* Criar verificação de existência de usuário antes do registro.
* Adicionar bloqueio de conta após múltiplas tentativas de login incorretas.
* Criar interface gráfica (GUI) para melhor experiência do usuário.

---

