from flask import Flask, jsonify, request, Response
from functools import wraps

app = Flask(__name__)

users = {
    "admin": "admin1",
    "user": "user1"
}
catalog = [
    {"id": 1, "name": "Coffe", "price": "50"},
    {"id": 2, "name": "Coffe2", "price": "55"},
    {"id": 3, "name": "Coffe3", "price": "60"}
]
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username in users and users[auth.username] == auth.password:
            return func(*args, **kwargs)
        return Response(
            jsonify({"error": "Authentication required"}), 401,
            headers={"WWW-Authenticate": "Basic realm='Login Required'"}
        )
    return wrapper
@app.route('/items', methods=['GET', 'POST'])
@authenticate
def items():
    if request.method == 'GET':
        return jsonify(catalog)
    elif request.method == 'POST':
        data = request.get_json()
        if not data or "id" not in data or "name" not in data or "price" not in data:
            return jsonify({"error": "Invalid data"}), 400
        if any(item["id"] == data["id"] for item in catalog):
            return jsonify({"error": "Item with this ID already exists"}), 400
        catalog.append(data)
        return jsonify({"message": "Item created successfully", "item": data}), 201
@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
@authenticate
def item_detail(item_id):
    item = next((i for i in catalog if i["id"] == item_id), None)
    if request.method == 'GET':
        if not item:
            return jsonify({"error": "Item not found"}), 404
        return jsonify(item)
    elif request.method == 'PUT':
        if not item:
            return jsonify({"error": "Item not found"}), 404
        data = request.get_json()
        if not data or "name" not in data or "price" not in data:
            return jsonify({"error": "Invalid data"}), 400
        item["name"] = data["name"]
        item["price"] = data["price"]
        return jsonify({"message": "Item updated successfully", "item": item})
    elif request.method == 'DELETE':
        if not item:
            return jsonify({"error": "Item not found"}), 404
        catalog.remove(item)
        return jsonify({"message": "Item deleted successfully"})
if __name__ == '__main__':
    app.run(debug=True)