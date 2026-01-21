from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Rota raiz (evita erro 404 no Render)
@app.route("/")
def home():
    return "Nexus Gestão está online 🚀"

# Rota da IA
@app.route("/pergunta", methods=["POST"])
def responder():
    dados = request.get_json()
    pergunta = dados.get("pergunta", "").lower()

    # Perguntas e respostas (você pode adicionar mais)
    if "olá" in pergunta or "oi" in pergunta:
        resposta = "Oi! Eu sou a IA do Nexus Gestão 😄"

    elif "arquivo" in pergunta or "arquivos" in pergunta:
        resposta = "Você pode acessar seus arquivos pelo botão de Gestão de Arquivos 📂"

    elif "botão" in pergunta:
        resposta = "Para criar um botão em HTML, use a tag <button>."

    elif "css" in pergunta:
        resposta = "CSS serve para estilizar o site: cores, fontes, layout."

    elif "javascript" in pergunta or "js" in pergunta:
        resposta = "JavaScript deixa o site interativo."

    elif "ia" in pergunta:
        resposta = "Eu sou uma IA simples baseada em regras, mas posso evoluir 😈"

    else:
        resposta = "Ainda não sei responder isso, mas estou aprendendo 👀"

    return jsonify({"resposta": resposta})


# ⚠️ ESSA PARTE É O QUE FAZ O RENDER FUNCIONAR
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
