# API_Clima
_____________________________________________________

## Instalacao
_____________________________________________________
 - Instalar Python 3.8
 - Verificar se possui o pip instalado
   $ pip -v
   $ wget https://bootstrap.pypa.io/get-pip.py
   $ sudo python get-pip.py
   
 - Instalar virtualenv
   $ pip install virtualenv 
   $ virtualenv nome_da_virtualenv
 
 - Ativar a virtualenv
   $ source nome_da_virtualenv/bin/activate (Linux ou macOS)
   $ nome_da_virtualenvScriptsactivate (Windows)
   
 - Instalar as dependencias
   $ pip install -r requirements.txt (buscar path do arquivo)
   
 - Instalar pipvenv
   $ pip install pipenv
   
 - Restaurar banco Postgres
   Considerar instalacao do Postgres
   Base (https://www.devmedia.com.br/instalando-postgresql/23364)
   Habilitar no arquivo .config alterando seguranca peer para md5 conforme link.
 

## Dependencias
_____________________________________________________
  A lista de dependencias se encontra no requiriments.txt e .lock

## Estrutura
_____________________________________________________
  A estrutura e basica considerando um arquivo principal app.py. 
  Foi considerada uma pasta segmentada para front, sendo a pasta templates.
  Como se trata de um projeto simples foi considerado todo o projeto em uma unica estrutura principal. Porem poderia ter sido segmentado em arquivo Model, View e app.
  O sistema se baseia em uma estrutura Flask Framework.
  

## Funcionamento
_____________________________________________________
  O funcionamento se deve ao rodar o comando 'flask run'.
  Neste ponto permitira que a pagina 'localhost:5000' redirecione a uma tela de pesquisa com uma cidade padrao para realizar a amostragem da consulta do API solicitado.
  Posterior a cada pesquisa dado pelo nome da cidade, os dados mostrados sao atualizados e os dados sao gravados no banco de dados.
  O sistema foi constituido em sistema linux Ubuntu 20.04.
  O sistema JSON para consulta com API e possivel consultar a partir do path 'localhost:5000/api/{nome da cidade}'.
  
 

