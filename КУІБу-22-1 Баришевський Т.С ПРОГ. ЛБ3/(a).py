from flask import Flask, jsonify

app = Flask(__name__)
catalog = [
    {"id": 1, "name": "Coffe", "price": "50"},
    {"id": 2, "name": "Coffe2", "price": "55"},
    {"id": 3, "name": "Coffe3", "price": "60"}
]
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(catalog)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in catalog if i["id"] == item_id))
    return jsonify(item)
if __name__ == '__main__':
    app.run(debug=True)