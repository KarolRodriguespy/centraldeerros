# Central de Erros    [![Build Status](https://travis-ci.com/KarolRodriguespy/centraldeerros.svg?branch=master)](https://travis-ci.com/KarolRodriguespy/centraldeerros)

## Objetivo

Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.


### Ferramentas Usadas

* Django
* Django Rest Framework
* Authentication Token
* Postgress


Documentação API:



### Como baixar os arquivos

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

-  Crie um usuario

 >

     python manage.py shell 
     from django.contrib.auth.models import User   
     user = User.objects.create_user('<yourname>', password='<password>')
     user.save()   
     
- Rode o servidor 

 >

       python manage.py runserver
       
- Crie o Token

 >

       Acesse o link: http://projeto-centraldeerros.herokuapp.com/get_token/ e informe o seu usuário e senha no body da requisição
- Para visualizar os eventos:

>

       Acesse o http://projeto-centraldeerros.herokuapp.com/events/list e informe o seu token no header da sua requisição

             