from PIL import Image
import os

# Diretório de saída
caminho_saida = r'C:\Users\junio\Downloads\dasdadasdasdsa'

# Pasta de entrada
pasta = r'C:\Users\junio\Downloads\testesasasas'

# Lê arquivos na pasta
arquivos = os.listdir(pasta)
for arquivo in arquivos:
    # Abre a imagem
    imagem = Image.open(os.path.join(pasta, arquivo))
    
    # Redimensiona mantendo a proporção
    width, height = 1000, 1000
    imagem.thumbnail((width, height))
    
    # Cria uma nova imagem com fundo branco
    imagem_final = Image.new("RGB", (width, height), "white")
    
    # Calcula a posição para centralizar a imagem redimensionada
    left = (width - imagem.width) // 2
    top = (height - imagem.height) // 2
    
    # Coloca a imagem redimensionada na imagem final
    imagem_final.paste(imagem, (left, top))
    
    # Salva a imagem final
    caminho_saida_arquivo = os.path.join(caminho_saida, arquivo)
    imagem_final.save(caminho_saida_arquivo)
