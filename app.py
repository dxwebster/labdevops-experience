from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)      

@app.route("/")
def pagina_inicial():
    return "Olá LAB Devops! Essa é a nova mensagem de saudação!"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)