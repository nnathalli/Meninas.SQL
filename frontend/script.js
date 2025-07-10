function mostrarSecao(id) {
  document.querySelectorAll(".secao").forEach(secao => secao.classList.remove("ativa"));
  document.getElementById(id).classList.add("ativa");
}

document.addEventListener("DOMContentLoaded", () => {
  carregarIntegrantes();
  carregarFrentes();
  carregarAtividades();
});

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

  try {
    const res = await fetch("/api/frentes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao cadastrar frente");

    alert("Frente cadastrada com sucesso!");
    e.target.reset();
    carregarFrentes();
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
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

async function atualizarFrente(codigo, data) {
  try {
    const res = await fetch(`/api/frentes/${codigo}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao atualizar frente");

    alert("Frente atualizada!");
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
}

async function removerFrente(codigo) {
  try {
    const res = await fetch(`/api/frentes/${codigo}`, { method: "DELETE" });
    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao remover frente");

    alert("Frente removida!");
    carregarFrentes();
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
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

  try {
    const res = await fetch("/api/atividades", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });

    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao cadastrar atividade");

    alert("Atividade cadastrada com sucesso!");
    e.target.reset();
    carregarAtividades();

  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
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
  try {
    const res = await fetch(`/api/atividades/${codigo}`, { method: "DELETE" });
    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao remover atividade");

    alert("Atividade removida!");
    carregarAtividades();
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
}


// --------- CADASTRO GERAL ---------
document.getElementById("form-geral").addEventListener("submit", async e => {
  e.preventDefault();
  const dadosIntegrante = {
    matricula: matricula.value,
    nome: nome.value,
    data_nasc: data_nasc.value,
    data_entrada: data_entrada.value,
    email: email.value,
    telefone: telefone.value
  };
  const tipo = document.getElementById("tipo-integrante").value;

  try {
    const res = await fetch("/api/integrantes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dadosIntegrante)
    });

    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao cadastrar integrante");

    sessionStorage.setItem("matriculaCadastro", dadosIntegrante.matricula);
    document.getElementById("cadastro-geral").style.display = "none";

    if (tipo === "professora") {
      document.getElementById("cadastro-professora").style.display = "block";
    } else {
      document.getElementById("cadastro-aluna").style.display = "block";
    }
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
});

async function atualizarIntegrante(matricula, data) {
  try {
    const res = await fetch(`/api/integrantes/${matricula}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao atualizar integrante");

    alert("Integrante atualizado!");
    carregarIntegrantes();
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
}

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
      <button onclick='preencherFormularioEdicaoIntegrante(${JSON.stringify(i)})'>Editar</button>
    `;
    ul.appendChild(li);
  });
}

async function removerIntegrante(matricula) {
  await fetch(`/api/integrantes/${matricula}`, { method: "DELETE" });
  carregarIntegrantes();
}

// --------- PROFESSORA ---------
document.getElementById("form-professora").addEventListener("submit", async e => {
  e.preventDefault();
  const dados = {
    matricula: sessionStorage.getItem("matriculaCadastro"),
    area_atuacao: document.getElementById("areaAtuacao").value,
    curriculo: document.getElementById("curriculo").value,
    instituicao: document.getElementById("instituicaoProf").value
  };

  try {
    const res = await fetch("/api/professoras", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados)
    });

    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao cadastrar professora");

    alert("Professora cadastrada com sucesso!");
    location.reload();
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
});

async function carregarProfessoras() {
  const res = await fetch("/api/professoras");
  const lista = await res.json();
  console.log("Professoras:", lista);
}

async function atualizarProfessora(matricula, data) {
  try {
    const res = await fetch(`/api/professoras/${matricula}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao atualizar professora");

    alert("Professora atualizada!");
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
}

async function removerProfessora(matricula) {
  await fetch(`/api/professoras/${matricula}`, {
    method: "DELETE"
  });
  alert("Professora removida!");
}

// --------- ALUNA ---------
document.getElementById("form-aluna").addEventListener("submit", async e => {
  e.preventDefault();
  const dados = {
    matricula: sessionStorage.getItem("matriculaCadastro"),
    bolsa: document.getElementById("bolsa").value === "true",
    nomecurso: document.getElementById("nomeCurso").value,
    instituicaocurso: document.getElementById("instituicaoCurso").value,
    departamento: document.getElementById("departamento").value,
    instituicao: document.getElementById("instituicaoAluna").value
  };

  try {
    const res = await fetch("/api/alunas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados)
    });

    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao cadastrar aluna");

    alert("Aluna cadastrada com sucesso!");
    location.reload();
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
});

async function carregarAlunas() {
  const res = await fetch("/api/alunas");
  const lista = await res.json();
  console.log("Alunas:", lista);
}

async function atualizarAluna(matricula, data) {
  try {
    const res = await fetch(`/api/alunas/${matricula}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const resposta = await res.json();

    if (!res.ok) throw new Error(resposta.erro || "Erro ao atualizar aluna");

    alert("Aluna atualizada!");
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
}

async function removerAluna(matricula) {
  await fetch(`/api/alunas/${matricula}`, {
    method: "DELETE"
  });
  alert("Aluna removida!");
}
