from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/pergunta", methods=["POST"])
def responder():
    dados = request.get_json()
    pergunta = dados.get("pergunta", "").lower()

    # --- Perguntas específicas ---
    if all(word in pergunta for word in ["botão", "arquivo"]):
        resposta = "Você pode criar um botão na gestão de arquivos usando o menu de edição."
    elif all(word in pergunta for word in ["abrir", "arquivo"]):
        resposta = "Você pode abrir seus arquivos no botão de gestão 📂."
    elif all(word in pergunta for word in ["salvar", "arquivo"]):
        resposta = "Para salvar, clique no botão de salvar dentro da gestão de arquivos 💾."
    elif all(word in pergunta for word in ["deletar", "arquivo"]):
        resposta = "Para deletar um arquivo, selecione ele e clique no botão de deletar 🗑️."
    elif all(word in pergunta for word in ["adicionar", "arquivo"]):
        resposta = "Use o botão 'Adicionar Arquivo' para criar um novo documento 📄."
    elif all(word in pergunta for word in ["editar", "arquivo"]):
        resposta = "Clique no arquivo que deseja editar e use o editor interno ✏️."
    elif all(word in pergunta for word in ["upload", "arquivo"]):
        resposta = "Você pode fazer upload de arquivos usando o botão de importação ⬆️."
    elif all(word in pergunta for word in ["download", "arquivo"]):
        resposta = "Clique no arquivo e depois em 'Download' para salvar no seu computador 💾."
    elif all(word in pergunta for word in ["configuração", "usuário"]):
        resposta = "Acesse o menu de configurações para alterar dados do usuário ⚙️."
    elif all(word in pergunta for word in ["esqueci", "senha"]):
        resposta = "Você pode redefinir sua senha clicando em 'Esqueci minha senha' 🔑."
    elif all(word in pergunta for word in ["login", "problema"]):
        resposta = "Verifique seu email e senha, e tente novamente ou use 'Esqueci minha senha'."
    elif all(word in pergunta for word in ["como", "logout"]):
        resposta = "Para sair, clique no botão de logout no canto superior direito ⏹️."
    elif all(word in pergunta for word in ["criar", "pasta"]):
        resposta = "Clique em 'Adicionar Pasta' para criar novas pastas 📁."
    elif all(word in pergunta for word in ["mover", "arquivo"]):
        resposta = "Arraste o arquivo para a pasta desejada ou use o botão de mover ↪️."
    elif all(word in pergunta for word in ["pesquisar", "arquivo"]):
        resposta = "Use a barra de pesquisa no topo para encontrar arquivos 🔍."
    elif all(word in pergunta for word in ["suporte", "ajuda"]):
        resposta = "Entre em contato com o suporte pelo botão de ajuda no canto inferior direito 🆘."

    # --- Perguntas genéricas ---
    elif "olá" in pergunta or "oi" in pergunta:
        resposta = "Oii! tudo bem? Eu sou Sun, a IA do Nexus Gestão 😎"
    elif "arquivo" in pergunta:
        resposta = "Você pode acessar seus arquivos no botão de gestão 📂."
    elif "senha" in pergunta:
        resposta = "Se você esqueceu a senha, clique em 'Esqueci minha senha' 🔑."
    elif "login" in pergunta:
        resposta = "Para entrar, use seu email e senha cadastrados no sistema."

    # --- Caso não reconheça ---
    else:
        resposta = "Não sei responder isso ainda, mas estou aprendendo! 🤖"

    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)