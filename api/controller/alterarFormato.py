from PIL import Image
import os
from flask import jsonify

def convert_webp_to_jpg(input_file, output_file):
    try:
        with Image.open(input_file) as img:
            if img.mode == 'CMYK':
                img = img.convert('RGB')
            img.save(output_file, 'JPEG')
        return True
    except IOError:
        return False

def convert_image(request, UPLOAD_FOLDER, OUTPUT_FOLDER):
    # Verifica se o arquivo webp foi enviado
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']

    # Verifica se o arquivo é uma imagem webp
    if file.filename.lower().endswith('.webp'):
        # Salva o arquivo temporariamente
        temp_file = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(temp_file)

        # Define o nome do arquivo de saída
        output_file = os.path.join(OUTPUT_FOLDER, os.path.splitext(file.filename)[0] + '.jpg')

        # Converte o arquivo webp para jpeg
        success = convert_webp_to_jpg(temp_file, output_file)

        # Remove o arquivo temporário
        os.remove(temp_file)

        if success:
            return jsonify({'message': 'Conversão bem-sucedida', 'output_file': output_file}), 200
        else:
            return jsonify({'error': 'Falha na conversão'}), 500
    else:
        return jsonify({'error': 'O arquivo não é uma imagem webp'}), 400
