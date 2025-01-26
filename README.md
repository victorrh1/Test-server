# Simple HTTP Server Test

Este projeto é um servidor HTTP simples, criado com a biblioteca padrão do Python. Ele é um ponto de partida para o desenvolvimento de uma API maior no futuro. O servidor responde a requisições GET e retorna uma página HTML básica com informações sobre o diretório requisitado.
Estrutura do Código

    Bibliotecas Utilizadas:
    O código utiliza http.server, uma biblioteca nativa do Python para criar servidores HTTP básicos.

    Classes e Métodos Principais:
        SimpleHandler: Classe que herda de BaseHTTPRequestHandler. Ela lida com requisições HTTP.
            do_GET(self): Método que responde a requisições GET. Ele:
                Envia o status HTTP 200 (OK).
                Define cabeçalhos HTTP, incluindo o tipo de conteúdo como HTML e um cabeçalho personalizado chamado Teste.
                Escreve um corpo HTML na resposta, que inclui o caminho requisitado (self.path).

    Servidor:
    O servidor é iniciado na porta 8000 do localhost usando a classe HTTPServer.

# Como Usar

    Certifique-se de ter o Python instalado (versão 3.6 ou superior).
    Execute o código com o comando:

    python server.py

    Acesse o servidor no navegador:
http://localhost:8000


