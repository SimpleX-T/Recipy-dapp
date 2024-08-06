from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
recipes = []
user_id_counter = 1
recipe_id_counter = 1



@app.route('/register', methods=['POST'])
def register():
    global user_id_counter
    username = request.json.get('username')
    if username in users:
        return jsonify({"message": "Username already exists."}), 400
    users[username] = user_id_counter
    user_id_counter += 1
    return jsonify({"message": "User registered successfully."}), 201

# Recipe submission endpoint
@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    global recipe_id_counter
    data = request.json
    title = data.get('title')
    ingredients = data.get('ingredients')
    instructions = data.get('instructions')
    user_id = data.get('user_id')

    recipe = {
        "id": recipe_id_counter,
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions,
        "user_id": user_id
    }
    recipes.append(recipe)
    recipe_id_counter += 1
    return jsonify({"message": "Recipe submitted successfully."}), 201

# Retrieve all recipes endpoint
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipes), 200

if __name__ == '__main__':
    app.run(debug=True)