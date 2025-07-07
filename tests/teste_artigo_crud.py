from src.persistence.artigo_crud import *
from datetime import date

# print("🔸 Criando artigo com PDF...")
# create_artigo(
#     codigo=1,
#     nome="Introdução à Inteligência Artificial",
#     publicacao="Revista de Computação",
#     data=date(2025, 6, 15),
#     autor="Maria Eduarda Pacheco",
#     caminho_pdf="tests/imagens/artigo_teste.pdf"  # ajuste conforme o local do PDF de teste
# )

print("\n🔸 Inserindo/atualizando PDF no artigo existente...")
upload_pdf_artigo(
    codigo=1,
    caminho_pdf="tests/imagens/livro_teste.pdf"  
)

print("\n🔸 Listando artigos...")
artigos = get_artigos()
for artigo in artigos:
    print(artigo)

print("\n🔸 Atualizando artigo...")
update_artigo(
    codigo=1,
    nome="Introdução à Inteligência Artificial - Atualizado",
    publicacao="Revista Brasileira de Computação",
    data=date(2025, 6, 20),
    autor="Maria Eduarda Pacheco"
)

print("\n🔸 Listando novamente após atualização...")
artigos = get_artigos()
for artigo in artigos:
    print(artigo)

print("\n🔸 Baixando PDF do artigo...")
download_pdf_artigo(1, "saida/artigo_baixado.pdf")

print("\n✅ Teste de artigo concluído com sucesso.")
