from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Olá LAB Devops! Essa é a nova mensagem de saudação!"

if __name__ == '__main__':
    app.run()