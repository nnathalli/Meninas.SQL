from src.persistence.frente_crud import *

from datetime import date

print("🔸 Criando frente de trabalho...")
create_frente(
    1,
    "Desenvolvimento de Jogos",
    "Extensão",
    "Grupo focado em desenvolvimento lúdico e gamificação",
    date.today()
)

print("🔸 Buscando frentes...")
for f in get_frentes():
    print(f)

print("🔸 Atualizando frente...")
update_frente(
    1,
    "Desenvolvimento de Jogos Digitais",
    "Extensão",
    "Agora com foco em jogos digitais e mobile",
    date.today()
)

print("🔸 Buscando novamente...")
for f in get_frentes():
    print(f)

# Descomente para deletar:
# print("🔸 Deletando frente...")
# delete_frente(1)

print("✅ Teste de frente finalizado.")
