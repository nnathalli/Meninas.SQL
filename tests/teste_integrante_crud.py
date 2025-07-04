from src.persistence.integrante_crud import *

from datetime import date

print("🔸 Criando integrante...")
create_integrante(
    "221000000",
    "Nathalli Maciel",
    date(2004, 2, 13),
    date(2025, 2, 15),
    "nathalli@unb.br",
    "(61)98231-0000"
)

print("🔸 Buscando integrantes...")
integrantes = get_integrantes()
for i in integrantes:
    print(i)

print("🔸 Atualizando integrante...")
update_integrante(
    "221010000",
    "Nathalli Maciel da Silva",
    date(2004, 6, 10),
    date(2025, 2, 15),
    "nathalli@unb.br",
    "(61)99876-0000"
)

print("🔸 Buscando novamente...")
for i in get_integrantes():
    print(i)

# Descomente se quiser deletar o teste:
# print("🔸 Deletando integrante...")
# delete_integrante("202500001")

print("✅ Teste de integrante finalizado.")
