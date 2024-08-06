# Decentralized Recipe Sharing Platform

This project is a simple backend application for a decentralized recipe sharing platform built using python (Flask). It allows users to register, submit recipes, and retrieve all submitted recipes.

## Features

- **User Registration**: Users can register with a unique username.
- **Recipe Submission**: Registered users can submit recipes, including title, ingredients, and instructions.
- **Retrieve Recipes**: Users can retrieve a list of all submitted recipes.


## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- `pip` for installing Python packages.

### Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. install Flask:

    ```bash
    pip install Flask

3. Run the application:
    ```bash
    python app.py
The application will start running on http://127.0.0.1:5000.

### API Endpoints
1. User Registration
- Endpoint: /register
- Method: POST
- Request Body:

    ```json
    {
        "username": "your_username"
    }

- Response:
    - Success: 201 Created
    ```json
    {
        "message": "User registered successfully."
    }
    ```
    - Error: 400 Bad Request (if the username already exists)
    ```json
    {
        "message": "Username already exists."
    }
    ```
2. Submit Recipe
- Endpoint: /submit_recipe
- Method: POST
- Request Body:
    ```json
    {
        "title": "Recipe Title",
        "ingredients": "List of ingredients",
        "instructions": "Cooking instructions",
        "user_id": 1
    }
    ```
- Response:
    - Success: 201 Created
    ```json
    {
        "message": "Recipe submitted successfully."
    }
    ```
3. Retrieve All Recipes
- Endpoint: /recipes
- Method: GET
- Response:
    - 200 OK
    ```json
    [
        {
            "id": 1,
            "title": "Recipe Title",
            "ingredients": "List of ingredients",
            "instructions": "Cooking instructions",
            "user_id": 1
        },
        ...
    ]
    ```

### Thank you cartesi for this oppurtunity to learn 🙏🏽