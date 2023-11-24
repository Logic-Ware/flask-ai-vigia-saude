from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle


app = Flask(__name__)
CORS(app)

with open('modelo_IF.pickle', 'rb') as f:  # Este arquivo está no zip da entrega, pode ser necessário ajustar o caminho.
    modelo_ia = pickle.load(f)

# Rota para receber os dados e fazer previsões com o modelo
@app.route('/prever', methods={'GET'})


def prever():
    # Obter parâmetros da solicitação GET
    taxa_incidencia = float(request.args.get('tx_incd'))

    # Fazer previsões usando o modelo
    resultado = modelo_ia.predict([[taxa_incidencia]])

    return jsonify({'previsao': resultado.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
