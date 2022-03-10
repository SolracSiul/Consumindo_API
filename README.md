# **Code Challenge Mundo DevOps**
## **Projeto MundoDevOps**

O projeto tinha como objetivo principal construir uma API que realizesse interação com a [IP_API](https://ip-api.com/docs/api:json) e salvasse os dados 
em um banco de dados.

## **Tecnologias**
- Python
- Django restframework

## **Objetivos**
- Constrir a minha própria API 
- Realizar a interação com IP_API
- Criar dois endpoints: 
       - Consultar IP e retornar as informações
       - Retornar o histórico das últimas requisições

## **Execução do projeto**

Primeiramente é necessário instalar o [Python](https://www.python.org/) na sua máquina e instalar/utilizar sua IDE de prefência.
Abra o terminal e execute os seguintes comandos:
```sh
pip install djangorestframework
pip install Django  
pip install requests
```
# **Após instalar as dependências necessárias execute o próximo comando:**
- Ele será responsável por rodar a aplicação:
```sh
py manage.py runserver
```
# **Testes**

### Agora chegou a parte mais interessante do projeto que é ver ele funcionando na prática! 
---
- Será necessário a instalação de uma aplicação chamada API Cliente, você pode utilizar a que preferir. Ela servirá para testar os endpoints.
---
- Nessa aplicação foi criado dois endpoints. São eles: **consultaIP/** e **historico/**

 ### Pronto, agora é só copiar o Starting development server at http://127.0.0.1:8000/ e  copiar no seu API_Cliente e utilizar os comandos 
    GET     http://127.0.0.1:8000/consultaIP/ (inserira_o_número_do_IP_que_deseja_consultar};
    GET     http://127.0.0.1:8000/historico/ . Com esse comando você tem o retorno do histórico de solicitações;



## Easter egg

##### Caso você deseje acessar o banco de dados dessa aplicação é só abrir o arquivo .db da aplicação com o software [db.browser](https://sqlitebrowser.org/)

___
                                                 Desenvolvido por Luis Carlos. @crluis521@gmail.com






