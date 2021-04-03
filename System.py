
import os

#Scrpit para intstalar os componentes basicos

os.system("sudo python3 -m pip install requests")
os.system("sudo apt-get install python3-requests")
os.system("sudo apt autoremove")
os.system("sudo apt-get build-dep python-psycopg2")
os.system("clear")

path = "virtualenv"

# Checa o diretorio atual.
retval = os.getcwd()
print ("Current working directory {}".format(retval))

# Altera o diretorio
os.chdir( path )

# Checa novo diretorio.
retval = os.getcwd()

print ("Directory changed successfully {}".format(retval))


#Ativar virtualenv
os.system("source bin/activate")

#instalar pacotes pip no virtualenv
os.system("pip3 install requests")
os.system("pip3 install psycopg2-binary")
os.system("pip3 install psycopg2")


#criar usuario
os.system("sudo -u postgres psql")




