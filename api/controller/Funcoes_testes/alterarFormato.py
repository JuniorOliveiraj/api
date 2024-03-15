from PIL import Image
import os

def convert_webp_to_jpg(input_file, output_file):
    try:
        # Open the WebP image
        with Image.open(input_file) as img:
            # Convert to RGB mode if the image is in CMYK mode
            if img.mode == 'CMYK':
                img = img.convert('RGB')

            # Save as JPG
            img.save(output_file, 'JPEG')

        print('Conversion successful!')

    except IOError:
        print(f'Unable to open {input_file}')

# Diretório de entrada (mesmo do código anterior)
pasta = r'C:\Users\junio\Downloads\testesasasas'

# Diretório de saída (mesmo do código anterior)
caminho_saida = r'C:\Users\junio\Downloads\dasdadasdasdsa'

# Lê arquivos na pasta
arquivos = os.listdir(pasta)
for arquivo in arquivos:
    # Verifica se o arquivo é uma imagem webp
    if arquivo.lower().endswith('.webp'):
        # Caminho do arquivo de entrada e saída
        input_file = os.path.join(pasta, arquivo)
        output_file = os.path.join(caminho_saida, os.path.splitext(arquivo)[0] + '.jpg')
        
        # Converte de webp para jpeg
        convert_webp_to_jpg(input_file, output_file)
