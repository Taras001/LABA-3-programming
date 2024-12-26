from flask import Flask, jsonify, request

app = Flask(__name__)
catalog = [
    {"id": 1, "name": "Coffe", "price": "50"},
    {"id": 2, "name": "Coffe2", "price": "55"},
    {"id": 3, "name": "Coffe3", "price": "60"}
]
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(catalog)
if __name__ == '__main__':
    app.run(debug=True)
