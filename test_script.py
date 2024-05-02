import subprocess
import subprocess





# Commandes Docker à exécuter
commands = [
    "docker pull maximed007/odoo:latest",
    "sudo docker-compose down",
    "sudo docker-compose up -d",
]



# Boucle sur chaque commande et l'exécute
for command in commands:
    subprocess.run(command, shell=True)




