# Central de Erros    

## Objetivo

Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.


### Ferramentas Usadas

* Django
* Django Rest Framework
* Authentication Token
* Postgress
* Heroku


[Documentação API](https://app.swaggerhub.com/apis-docs/KarolRodriguespy/centraldeerros/1.0.0) 

[link produção](https://projeto-centraldeerros.herokuapp.com/)

**Usuário para acesso:

username: admin
senha: 123456

### Para testar Localmente

-  Faça uma cópia do repositório na sua máquina
>

     git clone https://github.com/KarolRodriguespy/AceleraDev_Python.git 

- Crie um novo ambiente virtual e ative 

Windows
>

      python -m venv env 
      env\Scripts\activate.bat

 MAC
 >

      python3 -m venv env 
      source env/bin/activate
 
 
- Instale as dependencias do arquivo requirements.txt 

 >

       pip install - r requirements.txt
     
      
      
      
-  Crie as migrations

 >

       python manage.py migrate
 
     
- Rode o servidor 

 >

       python manage.py runserver
       
- Crie um usuário:
 >

       Acesse o endereço: https://projeto-centraldeerros.herokuapp.com/rest-auth/registration/ e informe:
       - Um nome de usuário
       - email
       - Senha
       
       
- Crie o Token

 >

       Acesse o link: https://projeto-centraldeerros.herokuapp.com/rest-auth/login/ e informe o seu usuário, email e senha
       
       
- Para visualizar os eventos:

>

       Acesse o http://projeto-centraldeerros.herokuapp.com/events/list e informe o seu token no header da sua requisição

             