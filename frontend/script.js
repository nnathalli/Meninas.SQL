// script.js COMPLETO - Atualizado com fetch, remoção de arrays locais e renderização do banco

document.addEventListener('DOMContentLoaded', () => {
    // ----------- INTEGRANTE -----------
    document.getElementById('form-integrante').addEventListener('submit', async (e) => {
        e.preventDefault();
        const form = e.target;
        const formData = new FormData();

        formData.append('matricula', form['integrante-matricula'].value);
        formData.append('nome', form['integrante-nome'].value);
        formData.append('data_nasc', form['integrante-data-nasc'].value);
        formData.append('data_entrada', form['integrante-data-entrada'].value);
        formData.append('email', form['integrante-email'].value);
        formData.append('telefone', form['integrante-telefone'].value);
        formData.append('foto', form['integrante-foto'].files[0]);

        try {
            const res = await fetch('/api/integrantes', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            if (res.ok) {
                alert(data.mensagem);
                form.reset();
                renderIntegrantes();
            } else {
                alert('Erro: ' + data.erro);
            }
        } catch (err) {
            alert('Erro de conexão: ' + err.message);
        }
    });


    const renderIntegrantes = async () => {
        try {
            const res = await fetch('/api/integrantes');
            const integrantes = await res.json();
            const tbody = document.getElementById('integrantes-table-body');
            tbody.innerHTML = '';
            integrantes.forEach((i, index) => {
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${i.matricula}</td>
                    <td>${i.nome}</td>
                    <td>${formatDate(i.data_nasc)}</td>
                    <td>${formatDate(i.data_entrada)}</td>
                    <td>${i.email}</td>
                    <td>${i.telefone}</td>
                    <td>
                        <button class="edit-btn" data-id="${i.matricula}">Editar</button>
                        <button class="delete-btn" data-id="${i.matricula}">Excluir</button>
                    </td>
                `;
            });
            document.getElementById('total-integrantes').textContent = integrantes.length;
        } catch (err) {
            console.error('Erro ao carregar integrantes:', err);
        }
    };

    // ----------- FRENTE -----------
    document.getElementById('form-frente').addEventListener('submit', async (e) => {
        e.preventDefault();
        const form = e.target;
        const frente = {
            codigo: form['frente-codigo'].value,
            nome: form['frente-nome'].value,
            tipo: form['frente-tipo'].value,
            descricao: form['frente-descricao'].value,
            data_criacao: form['frente-data-criacao'].value
        };

        try {
            const res = await fetch('/api/frentes', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(frente)
            });
            const data = await res.json();
            if (res.ok) {
                alert(data.mensagem);
                form.reset();
                renderFrentes();
            } else {
                alert('Erro: ' + data.erro);
            }
        } catch (err) {
            alert('Erro de conexão: ' + err.message);
        }
    });

    const renderFrentes = async () => {
        try {
            const res = await fetch('/api/frentes');
            const frentes = await res.json();
            const tbody = document.getElementById('frentes-table-body');
            tbody.innerHTML = '';
            frentes.forEach((f, index) => {
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${f.codigo}</td>
                    <td>${f.nome}</td>
                    <td>${f.tipo}</td>
                    <td>${f.descricao}</td>
                    <td>${formatDate(f.data_criacao)}</td>
                    <td>
                        <button class="edit-btn" data-id="${f.codigo}">Editar</button>
                        <button class="delete-btn" data-id="${f.codigo}">Excluir</button>
                    </td>
                `;
            });
            document.getElementById('total-frentes').textContent = frentes.length;
        } catch (err) {
            console.error('Erro ao carregar frentes:', err);
        }
    };

    // ----------- ATIVIDADE -----------
    document.getElementById('form-atividade').addEventListener('submit', async (e) => {
        e.preventDefault();
        const form = e.target;
        const atividade = {
            codigo: form['atividade-codigo'].value,
            nome: form['atividade-nome'].value,
            descricao: form['atividade-descricao'].value,
            tipo: form['atividade-tipo'].value,
            local: form['atividade-local'].value,
            data_hora: form['atividade-datahora'].value,
            duracao: form['atividade-duracao'].value
        };

        try {
            const res = await fetch('/api/atividades', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(atividade)
            });
            const data = await res.json();
            if (res.ok) {
                alert(data.mensagem);
                form.reset();
                renderAtividades();
            } else {
                alert('Erro: ' + data.erro);
            }
        } catch (err) {
            alert('Erro de conexão: ' + err.message);
        }
    });

    const renderAtividades = async () => {
        try {
            const res = await fetch('/api/atividades');
            const atividades = await res.json();
            const tbody = document.getElementById('atividades-table-body');
            tbody.innerHTML = '';
            atividades.forEach((a, index) => {
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${a.codigo}</td>
                    <td>${a.nome}</td>
                    <td>${a.tipo}</td>
                    <td>${a.local}</td>
                    <td>${formatDateTime(a.data_hora)}</td>
                    <td>${a.duracao}</td>
                    <td>
                        <button class="edit-btn" data-id="${a.codigo}">Editar</button>
                        <button class="delete-btn" data-id="${a.codigo}">Excluir</button>
                    </td>
                `;
            });
            document.getElementById('total-atividades').textContent = atividades.length;
        } catch (err) {
            console.error('Erro ao carregar atividades:', err);
        }
    };

    // ----------- FORMATADORES -----------
    const formatDate = (dateStr) => {
        if (!dateStr) return '';
        const date = new Date(dateStr);
        return date.toLocaleDateString('pt-BR');
    };

    const formatDateTime = (dateStr) => {
        if (!dateStr) return '';
        const date = new Date(dateStr);
        return date.toLocaleString('pt-BR');
    };

    // ----------- INICIAL -----------
    renderIntegrantes();
    renderFrentes();
    renderAtividades();
});
