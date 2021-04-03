from classes import Cidade
import psycopg2 as db
import json
import html


cidade = Cidade()

cidade.setNome(input("Insira o nome da Cidade que deseja saber o clima: "))

#Atualizacao dos dados consultando API
cidade.clima_temp()


#funcao de consuta no DB
def consulta():
    connection = None
    try:
        
        # connecta com o PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = db.connect(host="localhost",database="postgres",user="linx",password="linx_APi")
        connection.autocommit = True      

        #cria um cursor
        cur=connection.cursor()

        #Realiza consulta do banco      
        select_Query = "select * from api_table_clima"

        cur.execute(select_Query)
        print("Selecionando todas os dados da tabela")
        all_records = cur.fetchall()

        print("Print each row and it's columns values")
        for row in all_records:
            print("Nome = ", row[0]),
            print("Temperatura = ", row[1]),
            print("Velocidade do Vento  = ", row[2]),
            print("Humidade = ", row[3]),
            print("Pressao Atmosferica", row[4]),
            print("Longitude = ", row[5]),
            print("Latitude = ", row[6], "\n")


    except (Exception, db.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


#funcao de atualizacao do DB
def atualiza():
    connection = None
    try:
        
        # connecta com o PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = db.connect(host="localhost",database="postgres",user="linx",password="linx_APi")
        connection.autocommit = True      
		
        # cria um cursor
        cur = connection.cursor()

        cur.execute("INSERT into api_table_clima values ('{}','{}','{}','{}','{}','{}','{}')".format(cidade.getNome(), cidade.temperatura(), cidade.vento(), cidade.humidade(), cidade.pressao(), cidade.longitude(), cidade.latitude()))
        id = cur.fetchone()


    except (Exception, db.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

atualiza()
consulta()

