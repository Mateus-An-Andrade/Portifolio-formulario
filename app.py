from flask import Flask,render_template, request, jsonify
from back import inserir_dados

app = Flask (__name__)

@app.route('/')
def form():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])

def submit():
    try:
        print('submit chamado!')
        # Receber os dados do formulário
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        mensagem = request.form['mensagem']

        print(f"Tamanho do nome: {len(nome)} caracteres")
        print(f"Tamanho do telefone: {len(telefone)} caracteres")
        print((f"Tamanho do email: {len(email)} caracteres"))
        print(f"Tamanho da mensagem: {len(mensagem)} caracteres")



        if nome and telefone and email and mensagem:
            sucesso= inserir_dados(nome,telefone,email,mensagem)
            if sucesso:
                return 'dados enviados com sucesso!',200

            else:
                return 'Erro ao enviar o formulario!',500
        else:
            return 'Informações faltantes no formulario!',400    
    except Exception as e:
        print (f"Erro: {e}")
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)