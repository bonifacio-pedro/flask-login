# Sistema de login completo feio em Flask e Python!
Uma aplicação de login feita com Python, Flask, MySQL, Jinja, BootStrap5 e HTML5.
Contém as seguintes funcionalidades:

✅ Visualizar home específica por sessão (como com um usuário logado ou um visitante).
✅ Cadastrar e automaticamente depois ser levado a página de login, o cadastro é enviado ao banco de dados, a senha é criptografada pelo algoritmo Argon2
> context = CryptContext(schemes=['argon2'])
> self.passwd = context.hash(passwd)
✅ Sair da conta, trocar, e criar outra. Nenhuma funcionalidade é imposta uma sobre a outra, a sessão é excluida quando se da logout, assim ativando o cadastro e login novamente
✅ Página de administrador, onde é possivel analisar os usuários e seus ID's, sem visualização de senha, podendo excluir usuários, uma página "secreta" onde somente a sessão administrativa pode entrar

![Homepage](https://github.com/bonifacio-pedro/flask-login/blob/main/Homepage.png)
![Login](https://github.com/bonifacio-pedro/flask-login/blob/main/Login.png)
![Homepage logado](https://github.com/bonifacio-pedro/flask-login/blob/main/Homepage%20logado.png)
![Cadastro](https://github.com/bonifacio-pedro/flask-login/blob/main/Cadastro.png)
![ADM](https://github.com/bonifacio-pedro/flask-login/blob/main/Painel%20de%20administração.png)

