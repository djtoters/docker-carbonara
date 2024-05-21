from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Token d'authentification (vous pouvez le stocker de manière sécurisée dans une variable d'environnement)
SECRET_TOKEN = "YOUR_SECRET_TOKEN"

# Commandes Docker à exécuter
commands = [
    "docker pull toters/odoo:latest",
    "sudo docker-compose down",
    "sudo docker-compose up -d",
]

@app.route('/webhook', methods=['POST'])
def webhook():
    auth_header = request.headers.get('Authorization')
    if auth_header is None or not auth_header.startswith("Bearer "):
        return jsonify({"message": "Token manquant ou incorrect"}), 403
    
    token = auth_header.split(" ")[1]
    if token != SECRET_TOKEN:
        return jsonify({"message": "Token invalide"}), 403
    
    
    # Boucle sur chaque commande et l'exécute
    if token == SECRET_TOKEN & request.method == 'POST':
        for command in commands:
            subprocess.run(command, shell=True)
        return jsonify({"message": "Webhook reçu"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
