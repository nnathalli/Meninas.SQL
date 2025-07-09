let integrantes = [];
let frentes = [];
let atividades = [];

const formatDate = (dateString) => new Date(dateString + 'T00:00:00').toLocaleDateString('pt-BR');
const formatDateTime = (dateTimeString) => new Date(dateTimeString).toLocaleString('pt-BR', {
    year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit'
});

// ========== CARGA INICIAL ==========
async function carregarIntegrantes() {
    const res = await fetch('/api/integrantes');
    integrantes = await res.json();
    renderIntegrantes();
}

async function carregarFrentes() {
    const res = await fetch('/api/frentes');
    frentes = await res.json();
    renderFrentes();
}

async function carregarAtividades() {
    const res = await fetch('/api/atividades');
    atividades = await res.json();
    renderAtividades();
}

// ========== FORMULÁRIO DE INTEGRANTES ==========
document.getElementById('json-integrante').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const index = form['integrante-edit-index'].value;
    const integrante = {
        matricula: form['integrante-matricula'].value,
        nome: form['integrante-nome'].value,
        data_nasc: form['integrante-data-nasc'].value,
        data_entrada: form['integrante-data-entrada'].value,
        email: form['integrante-email'].value,
        telefone: form['integrante-telefone'].value
    };

    const url = index === '' ? '/api/integrantes' : `/api/integrantes/${integrante.matricula}`;
    const method = index === '' ? 'POST' : 'PUT';

    const res = await fetch(url, {
        method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(integrante)
    });

    if (res.ok) {
        alert(index === '' ? 'Integrante cadastrado!' : 'Integrante atualizado!');
        form.reset();
        form['integrante-edit-index'].value = '';
        await carregarIntegrantes();
    } else {
        const err = await res.json();
        alert('Erro: ' + err.erro);
    }
});

// ========== FORMULÁRIO DE FRENTES ==========
document.getElementById('form-frente').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const index = form['frente-edit-index'].value;
    const frente = {
        codigo: form['frente-codigo'].value,
        nome: form['frente-nome'].value,
        tipo: form['frente-tipo'].value,
        descricao: form['frente-descricao'].value,
        datacriacao: form['frente-data-criacao'].value
    };

    const url = index === '' ? '/api/frentes' : `/api/frentes/${frente.codigo}`;
    const method = index === '' ? 'POST' : 'PUT';

    const res = await fetch(url, {
        method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(frente)
    });

    if (res.ok) {
        alert(index === '' ? 'Frente cadastrada!' : 'Frente atualizada!');
        form.reset();
        form['frente-edit-index'].value = '';
        await carregarFrentes();
    } else {
        const err = await res.json();
        alert('Erro: ' + err.erro);
    }
});

// ========== FORMULÁRIO DE ATIVIDADES ==========
document.getElementById('form-atividade').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const index = form['atividade-edit-index'].value;
    const atividade = {
        codigo: form['atividade-codigo'].value,
        nome: form['atividade-nome'].value,
        descricao: form['atividade-descricao'].value,
        tipo: form['atividade-tipo'].value,
        local: form['atividade-local'].value,
        data_hora: form['atividade-datahora'].value,
        duracao: form['atividade-duracao'].value
    };

    const url = index === '' ? '/api/atividades' : `/api/atividades/${atividade.codigo}`;
    const method = index === '' ? 'POST' : 'PUT';

    const res = await fetch(url, {
        method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(atividade)
    });

    if (res.ok) {
        alert(index === '' ? 'Atividade cadastrada!' : 'Atividade atualizada!');
        form.reset();
        form['atividade-edit-index'].value = '';
        await carregarAtividades();
    } else {
        const err = await res.json();
        alert('Erro: ' + err.erro);
    }
});

// ========== RENDERIZAÇÃO ==========
function renderIntegrantes() {
    const tbody = document.getElementById('integrantes-table-body');
    tbody.innerHTML = '';
    integrantes.forEach((i, idx) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="py-2 px-4">${i.matricula}</td>
            <td class="py-2 px-4">${i.nome}</td>
            <td class="py-2 px-4">${formatDate(i.data_nasc)}</td>
            <td class="py-2 px-4">${formatDate(i.data_entrada)}</td>
            <td class="py-2 px-4">${i.email}</td>
            <td class="py-2 px-4">${i.telefone}</td>
            <td class="py-2 px-4">
                <button onclick="editarIntegrante(${idx})" class="bg-blue-500 text-white px-3 py-1 rounded mr-2">Editar</button>
                <button onclick="excluirIntegrante('${i.matricula}')" class="bg-red-500 text-white px-3 py-1 rounded">Excluir</button>
            </td>
        `;
        tbody.appendChild(row);
    });
    document.getElementById('total-integrantes').textContent = integrantes.length;
}

function renderFrentes() {
    const tbody = document.getElementById('frentes-table-body');
    tbody.innerHTML = '';
    frentes.forEach((f, idx) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="py-2 px-4">${f.codigo}</td>
            <td class="py-2 px-4">${f.nome}</td>
            <td class="py-2 px-4">${f.tipo}</td>
            <td class="py-2 px-4">${f.descricao}</td>
            <td class="py-2 px-4">${formatDate(f.datacriacao)}</td>
            <td class="py-2 px-4">
                <button onclick="editarFrente(${idx})" class="bg-blue-500 text-white px-3 py-1 rounded mr-2">Editar</button>
                <button onclick="excluirFrente('${f.codigo}')" class="bg-red-500 text-white px-3 py-1 rounded">Excluir</button>
            </td>
        `;
        tbody.appendChild(row);
    });
    document.getElementById('total-frentes').textContent = frentes.length;
}

function renderAtividades() {
    const tbody = document.getElementById('atividades-table-body');
    tbody.innerHTML = '';
    atividades.forEach((a, idx) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="py-2 px-4">${a.codigo}</td>
            <td class="py-2 px-4">${a.nome}</td>
            <td class="py-2 px-4">${a.tipo}</td>
            <td class="py-2 px-4">${a.local}</td>
            <td class="py-2 px-4">${formatDateTime(a.data_hora)}</td>
            <td class="py-2 px-4">${a.duracao}</td>
            <td class="py-2 px-4">
                <button onclick="editarAtividade(${idx})" class="bg-blue-500 text-white px-3 py-1 rounded mr-2">Editar</button>
                <button onclick="excluirAtividade('${a.codigo}')" class="bg-red-500 text-white px-3 py-1 rounded">Excluir</button>
            </td>
        `;
        tbody.appendChild(row);
    });
    document.getElementById('total-atividades').textContent = atividades.length;
}

// ========== AÇÕES DE EDIÇÃO ==========
function editarIntegrante(index) {
    const i = integrantes[index];
    const f = document.getElementById('json-integrante');
    f['integrante-edit-index'].value = index;
    f['integrante-matricula'].value = i.matricula;
    f['integrante-nome'].value = i.nome;
    f['integrante-data-nasc'].value = i.data_nasc;
    f['integrante-data-entrada'].value = i.data_entrada;
    f['integrante-email'].value = i.email;
    f['integrante-telefone'].value = i.telefone;
}

function editarFrente(index) {
    const f = frentes[index];
    const form = document.getElementById('form-frente');
    form['frente-edit-index'].value = index;
    form['frente-codigo'].value = f.codigo;
    form['frente-nome'].value = f.nome;
    form['frente-tipo'].value = f.tipo;
    form['frente-descricao'].value = f.descricao;
    form['frente-data-criacao'].value = f.datacriacao;
}

function editarAtividade(index) {
    const a = atividades[index];
    const form = document.getElementById('form-atividade');
    form['atividade-edit-index'].value = index;
    form['atividade-codigo'].value = a.codigo;
    form['atividade-nome'].value = a.nome;
    form['atividade-descricao'].value = a.descricao;
    form['atividade-tipo'].value = a.tipo;
    form['atividade-local'].value = a.local;
    form['atividade-datahora'].value = a.data_hora;
    form['atividade-duracao'].value = a.duracao;
}

// ========== AÇÕES DE EXCLUSÃO ==========
async function excluirIntegrante(matricula) {
    if (confirm('Tem certeza que deseja excluir este integrante?')) {
        await fetch(`/api/integrantes/${matricula}`, { method: 'DELETE' });
        await carregarIntegrantes();
    }
}

async function excluirFrente(codigo) {
    if (confirm('Tem certeza que deseja excluir esta frente?')) {
        await fetch(`/api/frentes/${codigo}`, { method: 'DELETE' });
        await carregarFrentes();
    }
}

async function excluirAtividade(codigo) {
    if (confirm('Tem certeza que deseja excluir esta atividade?')) {
        await fetch(`/api/atividades/${codigo}`, { method: 'DELETE' });
        await carregarAtividades();
    }
}

// ========== INICIALIZAÇÃO ==========
document.addEventListener('DOMContentLoaded', async () => {
    await carregarIntegrantes();
    await carregarFrentes();
    await carregarAtividades();
});
