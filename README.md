Blog Flask

Uma aplicação de blog leve construída com Python e Flask. Este projeto demonstra conceitos fundamentais do Flask, como rotas, templates (Jinja2), formulários e gerenciamento de dados em memória.

##Funcionalidades##

Listar posts — a página inicial exibe todos os posts publicados com resumo e metadados

Ler post — página dedicada para cada post com conteúdo completo

Criar post — formulário para escrever e publicar novos posts (título, autor, conteúdo)

Deletar post — remove qualquer post da página inicial ou da página de detalhes

Layout responsivo — interface limpa com tema escuro usando HTML e CSS

##Tecnologias Utilizadas##
Tecnologia	Finalidade
Python 3.x	Linguagem de programação
Flask	Framework web (rotas, templates, formulários)
Jinja2	Motor de templates HTML (incluído no Flask)
HTML + CSS	Interface frontend
📁 Estrutura do Projeto
flask-blog/
├── app.py               # Aplicação principal — rotas e lógica
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
└── templates/
    ├── base.html        # Layout base (cabeçalho, rodapé, estilos)
    ├── index.html       # Página inicial — lista de posts
    ├── post.html        # Página de detalhes do post
    └── new_post.html    # Formulário para criar um novo post

##Como Executar##

1. Clone ou baixe o projeto

2. Instale as dependências

pip install -r requirements.txt

3. Execute a aplicação

python app.py

4. Abra no navegador

http://localhost:5000

##Rotas##
Método	Rota	Descrição
GET	/	Lista todos os posts
GET	/post/<id>	Exibe um único post
GET/POST	/new	Formulário para criar um novo post
POST	/delete/<id>	Deleta um post pelo ID


##Observações##

Os posts são armazenados em memória (sem banco de dados). Os dados são resetados quando o servidor reinicia.

Este projeto é intencionalmente simples para servir como exemplo educacional para iniciantes em Python.

Pode ser expandido com: banco de dados SQLite, autenticação de usuários, upload de imagens, etc.
