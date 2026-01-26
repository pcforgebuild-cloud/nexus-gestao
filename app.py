from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Rota raiz
@app.route("/")
def home():
    return "Nexus Gestão está online 🚀"

# Rota da IA
@app.route("/pergunta", methods=["POST"])
def responder():
    dados = request.get_json()
    pergunta = dados.get("pergunta", "").lower()

    # Arquivo
    if all(word in pergunta for word in ["botão", "arquivo"]):
        resposta = "Você pode criar um botão na gestão de arquivos usando a planilha que esta o banco de dados."
    elif all(word in pergunta for word in ["abrir", "arquivo"]):
        resposta = "Você pode abrir seus arquivos no botão 'Gestão de Arquivos 📂'."

    # Repetido
    elif all(word in pergunta for word in ["adicionar", "arquivo"]):
        resposta = "Para adicionar um arquivo você precisa colocar o nome do arquivo na coluna de nomes no banco de dados, e, colocar o link da página ou algum link externo 📄."
    elif all(word in pergunta for word in ["criar", "arquivo"]):
        resposta = "Para adicionar um arquivo você precisa colocar o nome do arquivo na coluna de nomes no banco de dados, e, colocar o link da página ou algum link externo 📄."
    elif all(word in pergunta for word in ["crio", "arquivo"]):
        resposta = "Para adicionar um arquivo você precisa colocar o nome do arquivo na coluna de nomes no banco de dados, e, colocar o link da página ou algum link externo 📄."
    elif all(word in pergunta for word in ["editar", "arquivo"]):
        resposta = "Mude o link ou o nome do arquivo desejado no banco de dados ✏️."
    elif all(word in pergunta for word in ["edito", "arquivo"]):
        resposta = "Mude o link ou o nome do arquivo desejado no banco de dados ✏️."
    elif all(word in pergunta for word in ["pesquisar", "arquivo"]):
        resposta = "Use a barra de pesquisa na página 'Gestão de Arquivos' para encontrar um arquivo 🔍."
    elif all(word in pergunta for word in ["pesquiso", "arquivo"]):
        resposta = "Use a barra de pesquisa na página 'Gestão de Arquivos' para encontrar um arquivo 🔍."
    elif all(word in pergunta for word in ["salvar", "anotação"]):
        resposta = "Para salvar uma anotação, clique no botão salvar anotação, certifique-se que o nível de importância esteja selecionado em alguma das três opções. 💾."
    elif all(word in pergunta for word in ["salvo", "anotação"]):
        resposta = "Para salvar uma anotação, clique no botão salvar anotação, certifique-se que o nível de importância esteja selecionado em alguma das três opções. 💾."
    elif all(word in pergunta for word in ["deletar", "anotação"]):
        resposta = "Para deletar uma anotação, clique no botão de apagar da anotação que deseja excluir 🗑️."
    elif all(word in pergunta for word in ["deleto", "anotação"]):
        resposta = "Para deletar uma anotação, clique no botão de apagar da anotação que deseja excluir 🗑️."
    elif all(word in pergunta for word in ["download", "anotação"]):
        resposta = "Clique em 'Dowload' para baixar o arquivo desejado."
    elif all(word in pergunta for word in ["baixo", "anotação"]):
        resposta = "Clique em 'Dowload' para baixar o arquivo desejado."
    elif all(word in pergunta for word in ["configuração", "botão"]):
        resposta = "O menu de 'Configurações⚙️' fica na barra lateral esquerda."
    elif all(word in pergunta for word in ["configurações", "onde"]):
        resposta = "O menu de 'Configurações⚙️' fica na barra lateral esquerda."
    # Configurações
    elif all(word in pergunta for word in ["alterar", "modo"]):
        resposta = "Acessando o menu 'Configurações' e selecione o modo ao qual deseja."
    elif all(word in pergunta for word in ["altero", "modo"]):
        resposta = "Acessando o menu 'Configurações' e selecione o modo ao qual deseja."
    elif all(word in pergunta for word in ["alterno", "modo"]):
        resposta = "Acessando o menu 'Configurações' e selecione o modo ao qual deseja."
    elif all(word in pergunta for word in ["mudo", "modo"]):
        resposta = "Acessando o menu 'Configurações' e selecione o modo ao qual deseja."


    # Ajuda
    elif all(word in pergunta for word in ["preciso", "ajuda"]):
        resposta = "Entre em contato com o suporte pelo botão de ajuda 🆘."


    # Perguntas genéricas
    elif "olá" in pergunta or "oi" in pergunta:
        resposta = "Oii! Eu sou Sun, a nova IA do Nexus Manager 😎"
    elif "arquivo" in pergunta:
        resposta = "Você pode acessar seus arquivos no botão 'Gestão de Arquivos 📂'."
    elif "senha" in pergunta:
        resposta = "Se você esqueceu a senha, clique em 'Esqueci minha senha' 🔑."
    elif "login" in pergunta:
        resposta = "Para entrar, use seu email e senha cadastrados no sistema."

    # Caso não reconheça
    else:
        resposta = "Não sei responder isso ainda, mas estou aprendendo! 🤖"

    return jsonify({"resposta": resposta})


# Render / Replit
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
