from flask import Flask
from controller.alterarFormato import convert_image
from controller.rotasTest import About, Home
app = Flask(__name__)

@app.route('/')
def home():
    return Home()

@app.route('/about')
def about():
    return About()

@app.route('/convert', methods=['POST'])
def convert():
    return convert_image( app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER'])

if __name__ == "__main__":
    app.run(debug=True)
