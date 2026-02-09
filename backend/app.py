from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)

# CORS is actually NOT needed here because frontend is a server,
# but keeping it open does no harm
CORS(app)

@app.route('/api/quote', methods=['GET'])
def get_quote():
    try:
        response = requests.get('https://zenquotes.io/api/random', timeout=5)
        response.raise_for_status()

        data = response.json()[0]
        return jsonify({
            'quote': data['q'],
            'author': data['a']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
