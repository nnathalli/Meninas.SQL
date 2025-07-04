from src.persistence.atividade_crud import *

from datetime import datetime, timedelta

print("🔸 Criando atividade...")
create_atividade(
    1,
    "Oficina de Python",
    "Curso introdutório de programação em Python",
    "Curso",
    "Auditório ICC Sul",
    datetime(2025, 9, 10, 14, 0),
    timedelta(hours=2)
)

print("🔸 Buscando atividades...")
for a in get_atividades():
    print(a)

print("🔸 Atualizando atividade...")
update_atividade(
    1,
    "Oficina de Python Avançada",
    "Curso intermediário de Python com projetos",
    "Curso",
    "Auditório FAC",
    datetime(2025, 9, 11, 10, 0),
    timedelta(hours=3)
)

print("🔸 Buscando novamente...")
for a in get_atividades():
    print(a)

# Descomente para deletar:
# print("🔸 Deletando atividade...")
# delete_atividade(1)

print("✅ Teste de atividade finalizado.")
