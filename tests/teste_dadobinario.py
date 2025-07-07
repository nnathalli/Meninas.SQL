from src.persistence.integrante_crud import adicionar_foto_integrante
import os

CAMINHO_IMAGEM = "tests/imagens/foto_teste.jpg"
print(" Caminho da imagem:", CAMINHO_IMAGEM)
print(" Arquivo existe?", os.path.exists(CAMINHO_IMAGEM))

adicionar_foto_integrante("221000009", CAMINHO_IMAGEM)
