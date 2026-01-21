// ===== PLANILHA CSV =====
const LINK_PLANILHA_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTNVmbjqjbG0194p9YcH8OxKw00AJvNo2PrIF8GjsRM0wQLAQdUNSeDi1TndOn8bCylTwJmVyQMOW2m/pub?output=csv";

fetch(LINK_PLANILHA_CSV)
.then(res => res.text())
.then(texto => {
  const linhas = texto.split("\n");
  const container = document.getElementById("botoes-container");
  const sidebarBotoes = document.getElementById("sidebar-botoes");

  linhas.slice(1).forEach(linha => {
    if(!linha.trim()) return;
    const partes = linha.split(",");
    const nome = partes[0].replace(/"/g,"").trim();
    const link = partes[1].replace(/"/g,"").trim();

    // BOTÃO NA TELA PRINCIPAL
    const btn = document.createElement("div");
    btn.className = "botao-planilha";
    btn.innerText = nome;
    btn.onclick = () => window.open(link,"_blank");
    container.appendChild(btn);

    // BOTÃO NA SIDEBAR
    const btnSidebar = document.createElement("button");
    btnSidebar.innerText = nome;
    btnSidebar.onclick = () => window.open(link,"_blank");
    sidebarBotoes.appendChild(btnSidebar);
  });
});

// ===== SIDEBAR =====
const sidebar = document.getElementById("sidebar");
const toggleBtn = document.getElementById("toggleBtn");

sidebar.addEventListener("mouseleave",() => sidebar.classList.add("closed"));
toggleBtn.addEventListener("click", () => sidebar.classList.toggle("closed"));

// ===== FUNÇÃO GENÉRICA DE TROCA DE TELAS =====
function mostrarTela(telaAtiva){
  const telas = ["tela-inicial","painel-gestao","painel-financeiro","painel-anot","tela-config","tela-ia"];
  telas.forEach(id => {
    document.getElementById(id).style.display = (id === telaAtiva) ? "block" : "none";
  });
}

// ===== BOTÕES DE NAVEGAÇÃO =====
document.getElementById("btn-gestao").onclick = () => mostrarTela("painel-gestao");
document.getElementById("btn-financa").onclick = () => mostrarTela("painel-financeiro");
document.getElementById("btn-ver-anot").onclick = abrirAnotacoes;
document.getElementById("btn-sidebar-anot").onclick = abrirAnotacoes;
document.getElementById("btn-config").onclick = () => mostrarTela("tela-config");
document.getElementById("btn-ia").onclick = () => mostrarTela("tela-ia");

document.getElementById("btn-voltar-arquivos").onclick = () => mostrarTela("tela-inicial");
document.getElementById("btn-voltar-financeiro").onclick = () => mostrarTela("tela-inicial");
document.getElementById("btn-voltar-anot").onclick = () => mostrarTela("tela-inicial");
document.getElementById("btn-voltar-config").onclick = () => mostrarTela("tela-inicial");

// ===== BUSCA PLANILHAS =====
const campoPesquisa = document.getElementById("campoPesquisa");
campoPesquisa.addEventListener("input", function(){
  const texto = this.value.toLowerCase();
  const botoes = document.querySelectorAll(".botao-planilha");
  botoes.forEach(botao => {
    botao.style.display = botao.innerText.toLowerCase().includes(texto) ? "flex" : "none";
  });
});

// ===== ANOTAÇÕES =====
const btnSalvar = document.getElementById("btn-salvar-anot");
const blocoNotas = document.getElementById("bloco-notas");

btnSalvar.addEventListener("click", () => {
  const texto = blocoNotas.value.trim();
  if(!texto) return alert("Escreva algo antes de salvar");

  let notas = JSON.parse(localStorage.getItem("anotacoes")) || [];
  notas.push(texto);
  localStorage.setItem("anotacoes", JSON.stringify(notas));
  blocoNotas.value = "";
  alert("Anotação salva com sucesso! 💾");
});

function abrirAnotacoes(){
  mostrarTela("painel-anot");
  carregarAnotacoes();
}

function carregarAnotacoes(){
  const lista = document.getElementById("lista-anot");
  lista.innerHTML = "";
  let notas = JSON.parse(localStorage.getItem("anotacoes")) || [];
  notas.forEach((nota,index)=>{
    const div = document.createElement("div");
    div.style.border = "1px solid #00ffc3";
    div.style.padding = "15px";
    div.style.margin = "10px";
    div.style.borderRadius = "10px";

    div.innerHTML = `<p>${nota}</p>
      <button onclick="editarNota(${index})">✏️Editar</button>
      <button onclick="apagarNota(${index})">🗑️Apagar</button>`;

    lista.appendChild(div);
  });
}

function editarNota(i){
  let notas = JSON.parse(localStorage.getItem("anotacoes"));
  const novoTexto = prompt("Edite sua anotação:", notas[i]);
  if(novoTexto !== null){
    notas[i] = novoTexto;
    localStorage.setItem("anotacoes", JSON.stringify(notas));
    carregarAnotacoes();
  }
}

function apagarNota(i){
  let notas = JSON.parse(localStorage.getItem("anotacoes"));
  notas.splice(i,1);
  localStorage.setItem("anotacoes", JSON.stringify(notas));
  carregarAnotacoes();
}

// ===== MODO CLARO / ESCURO =====
document.getElementById("btn-modo-claro").onclick = () => document.body.classList.add("modo-claro");
document.getElementById("btn-modo-escuro").onclick = () => document.body.classList.remove("modo-claro");

async function enviarPergunta() {
    const pergunta = document.getElementById("inputPergunta").value;

    const resposta = await fetch("https://nexus-gestao-2j6c.onrender.com/pergunta",
       {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pergunta })
    })
    .then(res => res.json())
    .then(data => {
        
      document.getElementById("respostaIA").innerText = data.resposta;
    });
  }

