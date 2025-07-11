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


// --------- CADASTRO DE INTEGRANTE ---------
document.getElementById("form-integrante").addEventListener("submit", async e => {
  e.preventDefault();

  const data = {
    matricula: document.getElementById("matricula").value,
    nome: document.getElementById("nome").value,
    datanasc: document.getElementById("data_nasc").value,
    dataentrada: document.getElementById("data_entrada").value,
    email: document.getElementById("email").value,
    telefone: document.getElementById("telefone").value
  };
  
  const tipo = document.getElementById("tipo-integrante").value;
  try {
    const res = await fetch("/api/integrantes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const resposta = await res.json();
    if (!res.ok) throw new Error(resposta.erro || "Erro ao cadastrar integrante");

    sessionStorage.setItem("matriculaCadastro", data.matricula);
    document.getElementById("cadastro-geral").style.display = "none";

    if (tipo === "professora") {
      document.getElementById("cadastro-professora").style.display = "block";
    } else {
      document.getElementById("cadastro-aluna").style.display = "block";
      carregarCursos(); // ← isso é essencial
    }
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }

});

// // --------- EDIÇÃO DE INTEGRANTE ---------
// document.getElementById("form-editar-integrante").addEventListener("submit", async e => {
//   e.preventDefault();
//   const matricula = document.getElementById("edit-matricula").value;
//   const data = {
//     nome: document.getElementById("edit-nome").value,
//     datanasc: document.getElementById("edit-data_nasc").value,
//     dataentrada: document.getElementById("edit-data_entrada").value,
//     email: document.getElementById("edit-email").value,
//     telefone: document.getElementById("edit-telefone").value
//   };
//   try {
//     const res = await fetch(`/api/integrantes/${matricula}`, {
//       method: "PUT",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify(data)
//     });

//     const resposta = await res.json();
//     if (!res.ok) throw new Error(resposta.erro || "Erro ao atualizar integrante");

//     alert("Integrante atualizado com sucesso!");
//   } catch (err) {
//     alert("❌ Erro: " + err.message);
//   }
// });

// async function carregarIntegrantes() {
//   const res = await fetch("/api/integrantes");
//   const lista = await res.json();
//   const ul = document.getElementById("lista-integrantes");
//   ul.innerHTML = "";
//   lista.forEach(i => {
//     const li = document.createElement("li");
//     li.innerHTML = `
//       <strong>${i.nome}</strong> (${i.matricula}) - ${i.email}
//       <button onclick="removerIntegrante('${i.matricula}')">Excluir</button>
//       <button onclick='preencherFormularioEdicaoIntegrante(${JSON.stringify(i)})'>Editar</button>
//   `;
//   ul.appendChild(li);
//   });
// }

// async function removerIntegrante(matricula) {
//   await fetch(`/api/integrantes/${matricula}`, { method: "DELETE" });
//   carregarIntegrantes();
// }

// --------- PROFESSORA ---------
document.getElementById("form-professora").addEventListener("submit", async e => {
  e.preventDefault();
  const dados = {
    matricula: sessionStorage.getItem("matriculaCadastro"),
    areaatuacao: document.getElementById("areaatuacao").value,
    curriculo: document.getElementById("curriculo").value,
    instituicao: document.getElementById("instituicaoProf").value
  };
    console.log("🔎 Dados enviados para /api/professoras:", dados);
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

document.getElementById("editar-dados").style.display = "block";
  carregarIntegrantesParaEdicao();
  carregarFrentesParaEdicao();
  carregarAtividadesParaEdicao();

// --------- CURSO ---------
document.getElementById("form-curso").addEventListener("submit", async e => {
  e.preventDefault();

  const data = {
    nome: document.getElementById("nomeCurso").value,
    instituicao: document.getElementById("instituicaoCurso").value,
    departamento: document.getElementById("departamentoCurso").value
  };

  try {
    const res = await fetch("/api/cursos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const resposta = await res.json();
    if (!res.ok) throw new Error(resposta.erro || "Erro ao cadastrar curso");

    alert("Curso cadastrado com sucesso!");
    document.getElementById("form-curso").reset();
    
    // Atualiza a lista de cursos e seleciona o novo curso automaticamente
    await carregarCursos();
    const select = document.getElementById("codcurso");
    const novoCurso = Array.from(select.options).find(opt => 
      opt.text.includes(data.nome) && opt.text.includes(data.instituicao)
    );
    if (novoCurso) {
      select.value = novoCurso.value;
    }
  } catch (err) {
    alert("❌ Erro: " + err.message);
  }
});

// async function carregarCursos() {
//   const res = await fetch("/api/cursos");
//   const cursos = await res.json();
//   const select = document.getElementById("codcurso");


//   // Limpa o select antes de adicionar os novos
//   select.innerHTML = '<option disabled selected value="">Selecione um curso</option>';

//   cursos.forEach(curso => {
//     const opt = document.createElement("option");
//     opt.value = curso.codcurso;
//     opt.textContent = `${curso.nome} - ${curso.instituicao}`;
//     select.appendChild(opt);
//   });
// }

async function carregarCursos() {
  try {
    const res = await fetch("/api/cursos");
    
    if (!res.ok) {
      throw new Error(`Erro HTTP: ${res.status}`);
    }

    const cursos = await res.json();
    console.log("Cursos recebidos:", cursos); // Para debug
    
    const select = document.getElementById("codcurso");
    select.innerHTML = '<option disabled selected value="">Selecione um curso</option>';

    if (Array.isArray(cursos)) {
      cursos.forEach(curso => {
        const opt = document.createElement("option");
        opt.value = curso.codcurso; // Usar codigo (consistente com o backend)
        opt.textContent = `${curso.nome} - ${curso.instituicao}`;
        select.appendChild(opt);
      });
    } else {
      console.error("Resposta inesperada:", cursos);
      alert("Formato de cursos inválido recebido do servidor");
    }
  } catch (error) {
    console.error("Erro ao carregar cursos:", error);
    alert("Erro ao carregar cursos. Verifique o console para detalhes.");
  }
}

// --------- ALUNA ---------
document.getElementById("form-aluna").addEventListener("submit", async e => {
  e.preventDefault();
  const codcurso = document.getElementById("codcurso").value;

  const dados = {
    matricula: sessionStorage.getItem("matriculaCadastro"),
    bolsa: document.getElementById("bolsa").value === "true",
    codcurso: document.getElementById("codcurso").value
  };

  if (!codcurso || codcurso === "undefined") {
    alert("⚠️ Por favor, selecione um curso antes de finalizar o cadastro.");
    return;
  }

  // const dados = {
  //   matricula: sessionStorage.getItem("matriculaCadastro"),
  //   bolsa: document.getElementById("bolsa").value === "true",
  //   codcurso: parseInt(codcurso)
  // };

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


// ----------------------------
// SEÇÃO: Gerenciamento por Professoras
// ----------------------------

// INTEGRANTES
async function carregarIntegrantesParaEdicao() {
  const res = await fetch("/api/integrantes");
  const lista = await res.json();
  const tbody = document.querySelector("#tabela-integrantes tbody");
  tbody.innerHTML = "";
  lista.forEach(item => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${item.matricula}</td>
      <td>${item.nome}</td>
      <td>${item.email}</td>
      <td>
        <button onclick="editarIntegrante('${item.matricula}', '${item.nome}', '${item.email}')">✏️</button>
        <button onclick="removerIntegrante('${item.matricula}')">🗑️</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function preencherFormularioEdicao(item) {
  document.getElementById("edit-matricula").value = item.matricula;
  document.getElementById("edit-nome").value = item.nome;
  document.getElementById("edit-data_nasc").value = item.datanasc;
  document.getElementById("edit-data_entrada").value = item.dataentrada;
  document.getElementById("edit-email").value = item.email;
  document.getElementById("edit-telefone").value = item.telefone;
}


document.getElementById("form-editar-integrante").addEventListener("submit", async e => {
  e.preventDefault();
  const matricula = document.getElementById("edit-matricula").value;
  const data = {
    nome: document.getElementById("edit-nome").value,
    datanasc: document.getElementById("edit-data_nasc").value,
    dataentrada: document.getElementById("edit-data_entrada").value,
    email: document.getElementById("edit-email").value,
    telefone: document.getElementById("edit-telefone").value
  };
  const res = await fetch(`/api/integrantes/${matricula}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  const resposta = await res.json();
  if (!res.ok) return alert("❌ Erro ao atualizar integrante");
  alert(resposta.mensagem || "Integrante atualizado!");
  carregarIntegrantesParaEdicao();
});
//   alert((await res.json()).mensagem || "Integrante atualizado!");
//   carregarIntegrantesParaEdicao();
// });

async function removerIntegrante(matricula) {
  if (!confirm("Confirmar exclusão?")) return;
  await fetch(`/api/integrantes/${matricula}`, { method: "DELETE" });
  carregarIntegrantesParaEdicao();
}

// FRENTES
async function carregarFrentesParaEdicao() {
  const res = await fetch("/api/frentes");
  const lista = await res.json();
  const tbody = document.querySelector("#tabela-frentes tbody");
  tbody.innerHTML = "";
  lista.forEach(item => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${item.codigo}</td>
      <td>${item.nome}</td>
      <td>${item.tipo}</td>
      <td>
        <button onclick="editarFrente('${item.codigo}', '${item.nome}', '${item.tipo}', '${item.descricao}')">✏️</button>
        <button onclick="removerFrente('${item.codigo}')">🗑️</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function editarFrente(codigo, nome, tipo, descricao) {
  document.getElementById("edit-codfrente").value = codigo;
  document.getElementById("edit-nomefrente").value = nome;
  document.getElementById("edit-tipofrente").value = tipo;
  document.getElementById("edit-descricaofrente").value = descricao;
}

document.getElementById("form-editar-frente").addEventListener("submit", async e => {
  e.preventDefault();
  const codigo = document.getElementById("edit-codfrente").value;
  const data = {
    nome: document.getElementById("edit-nomefrente").value,
    tipo: document.getElementById("edit-tipofrente").value,
    descricao: document.getElementById("edit-descricaofrente").value,
    datacriacao: document.getElementById("edit-datacriacaofrente").value,
  };
  await fetch(`/api/frentes/${codigo}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  alert("Frente atualizada!");
  carregarFrentesParaEdicao();
});

async function removerFrente(codigo) {
  if (!confirm("Confirmar exclusão da frente?")) return;
  await fetch(`/api/frentes/${codigo}`, { method: "DELETE" });
  carregarFrentesParaEdicao();
}

// ATIVIDADES
async function carregarAtividadesParaEdicao() {
  const res = await fetch("/api/atividades");
  const lista = await res.json();
  const tbody = document.querySelector("#tabela-atividades tbody");
  tbody.innerHTML = "";
  lista.forEach(item => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${item.codigo}</td>
      <td>${item.nome}</td>
      <td>${item.descricao}</td>
      <td>
        <button onclick="editarAtividade('${item.codigo}', '${item.nome}', '${item.descricao}')">✏️</button>
        <button onclick="removerAtividade('${item.codigo}')">🗑️</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function editarAtividade(codigo, nome, descricao) {
  document.getElementById("edit-codatividade").value = codigo;
  document.getElementById("edit-nomeatividade").value = nome;
  document.getElementById("edit-descricaoatividade").value = descricao;
}

document.getElementById("form-editar-atividade").addEventListener("submit", async e => {
  e.preventDefault();
  const codigo = document.getElementById("edit-codatividade").value;
  const data = {
    nome: document.getElementById("edit-nomeatividade").value,
    descricao: document.getElementById("edit-descricaoatividade").value
  };
  await fetch(`/api/atividades/${codigo}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  alert("Atividade atualizada!");
  carregarAtividadesParaEdicao();
});

async function removerAtividade(codigo) {
  if (!confirm("Confirmar exclusão da atividade?")) return;
  await fetch(`/api/atividades/${codigo}`, { method: "DELETE" });
  carregarAtividadesParaEdicao();
}

// CarregarIntegrantes
async function carregarIntegrantes() {
  const res = await fetch("/api/integrantes");
  const lista = await res.json();

  const tbody = document.querySelector("#tabela-integrantes tbody");
  tbody.innerHTML = "";

  lista.forEach(item => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${item.matricula}</td>
      <td>${item.nome}</td>
      <td>${item.email}</td>
      <td>${item.telefone}</td>
    `;
    tbody.appendChild(tr);
  });
}

function editarIntegrante(matricula, nome, email, telefone) {
  document.getElementById("edit-matricula").value = matricula;
  document.getElementById("edit-nome").value = nome;
  document.getElementById("edit-email").value = email;
  document.getElementById("edit-telefone").value = telefone;

  document.getElementById("form-editar-integrante").style.display = "block";
}

async function carregarIntegrantesParaEdicao() {
  const res = await fetch("/api/integrantes");
  const integrantes = await res.json();
  const tabela = document.getElementById("tabela-edicao-integrantes");
  tabela.innerHTML = "";

  integrantes.forEach(item => {
    const linha = document.createElement("tr");
    linha.innerHTML = `
      <td>${item.matricula}</td>
      <td>${item.nome}</td>
      <td>${item.email}</td>
      <td>${item.telefone}</td>
      <td>
        <button onclick="editarIntegrante('${item.matricula}', '${item.nome}', '${item.email}', '${item.telefone}')">✏️</button>
        <button onclick="removerIntegrante('${item.matricula}')">🗑️</button>
      </td>
    `;
    tabela.appendChild(linha);
  });
}

