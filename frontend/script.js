function mostrarSecao(id) {
  document.querySelectorAll(".secao").forEach(secao => secao.classList.remove("ativa"));
  document.getElementById(id).classList.add("ativa");
}

document.addEventListener("DOMContentLoaded", () => {
  carregarIntegrantes();
  carregarFrentes();
  carregarAtividades();

  // INTEGRANTES
  document.getElementById("form-integrante").addEventListener("submit", async e => {
    e.preventDefault();
    const data = {
      matricula: matricula.value,
      nome: nome.value,
      data_nasc: data_nasc.value,
      data_entrada: data_entrada.value,
      email: email.value,
      telefone: telefone.value
    };
    await fetch("/api/integrantes", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
    e.target.reset();
    carregarIntegrantes();
  });
});

async function carregarIntegrantes() {
  const res = await fetch("/api/integrantes");
  const lista = await res.json();
  const ul = document.getElementById("lista-integrantes");
  ul.innerHTML = "";
  lista.forEach(i => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${i.nome}</strong> (${i.matricula}) - ${i.email}
      <button onclick="removerIntegrante('${i.matricula}')">Excluir</button>
    `;
    ul.appendChild(li);
  });
}

async function removerIntegrante(matricula) {
  await fetch(`/api/integrantes/${matricula}`, { method: "DELETE" });
  carregarIntegrantes();
}

// FRENTES
document.getElementById("form-frente").addEventListener("submit", async e => {
  e.preventDefault();
  const data = {
    codigo: codigoFrente.value,
    nome: nomeFrente.value,
    tipo: tipoFrente.value,
    descricao: descricaoFrente.value,
    datacriacao: datacriacaoFrente.value
  };
  await fetch("/api/frentes", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });
  e.target.reset();
  carregarFrentes();
});

async function carregarFrentes() {
  const res = await fetch("/api/frentes");
  const lista = await res.json();
  const ul = document.getElementById("lista-frentes");
  ul.innerHTML = "";
  lista.forEach(f => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${f.nome}</strong> (${f.codigo}) - ${f.tipo}
      <button onclick="removerFrente('${f.codigo}')">Excluir</button>
    `;
    ul.appendChild(li);
  });
}

async function removerFrente(codigo) {
  await fetch(`/api/frentes/${codigo}`, { method: "DELETE" });
  carregarFrentes();
}

// ATIVIDADES
document.getElementById("form-atividade").addEventListener("submit", async e => {
  e.preventDefault();
  const data = {
    codigo: codigoAtiv.value,
    nome: nomeAtiv.value,
    descricao: descricaoAtiv.value,
    tipo: tipoAtiv.value,
    local: localAtiv.value,
    data_hora: dataHoraAtiv.value,
    duracao: duracaoAtiv.value
  };
  await fetch("/api/atividades", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });
  e.target.reset();
  carregarAtividades();
});

async function carregarAtividades() {
  const res = await fetch("/api/atividades");
  const lista = await res.json();
  const ul = document.getElementById("lista-atividades");
  ul.innerHTML = "";
  lista.forEach(a => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${a.nome}</strong> (${a.codigo}) - ${a.tipo} em ${a.local}
      <button onclick="removerAtividade('${a.codigo}')">Excluir</button>
    `;
    ul.appendChild(li);
  });
}

async function removerAtividade(codigo) {
  await fetch(`/api/atividades/${codigo}`, { method: "DELETE" });
  carregarAtividades();
}
