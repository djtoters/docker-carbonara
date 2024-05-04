from flask import Flask, request
import subprocess

app = Flask(__name__)

# Commandes Docker à exécuter
commands = [
    "docker pull toters/odoo:latest",
    "sudo docker-compose down",
    "sudo docker-compose up -d",
]

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Boucle sur chaque commande et l'exécute
        for command in commands:
            subprocess.run(command, shell=True)
        return 'Webhook reçu', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
