from flask import Flask, jsonify

app = Flask(__name__)
def load_catalog():
    catalog = []
    with open('catalog.txt', 'r') as f:
        for line in f:
            item_id, name, price = line.strip().split(',')
            catalog.append({"id": int(item_id), "name": name, "price": price})
    return catalog
@app.route('/items', methods=['GET'])
def get_items():
    catalog = load_catalog()
    return jsonify(catalog)
if __name__ == '__main__':
    app.run(debug=True)
