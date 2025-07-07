from src.persistence.livro_crud import *
from datetime import date


#create_livro(
#    codigo=1,
#    nome="Introdução ao Python",
#    descricao="Livro didático de programação",
#    editora="UnB Press",
#    estoque=10,
#    caminho_pdf="tests/imagens/livro_teste.pdf"
#)

upload_pdf_livro(
    codigo=1,
    caminho_pdf="tests/imagens/livro_teste.pdf"
)


print(get_livros())


update_livro(
    codigo=1,
    nome="Introdução ao Python - Atualizado",
    descricao="Livro didático de programação com exemplos",
    editora="UnB Press",
    estoque=15
)

download_pdf_livro(1, "saida/livro_baixado.pdf")

# delete_livro(1)
