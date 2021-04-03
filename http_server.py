import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
import webbrowser as webcontet

#Dretorio dos arquivos
webdir = '.'

#porta de conexao para servidor HTTP
port = 5000

#Se tiver algum diretorio ou porta na linha de comando, sera adicionado
if len(sys.argv) > 1: webdir = sys.argv[1]
if len(sys.argv) > 2: port = sys.argv[2]

#imprime as configuracoes
print('webdir "{}", port {}'.format(webdir, port))


#muda para o diretorio de trabalho
os.chdir(webdir)

#configura o endereco do servidor
srvraddr = ('', port)

#cria o servidor HTTP
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)

#espera receber algum comando
srvrobj.serve_forever()

#permitir pagina cgi
webcontet.open(srvraddr+"cgi-bin/py.py")

