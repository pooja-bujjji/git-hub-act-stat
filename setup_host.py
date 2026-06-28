import os
import subprocess
import shutil

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


if shutil.which("nginx"):
    print("nginx already installed")
else:
    command = "sudo apt update && sudo apt install -y nginx"
    run(command)

run("sudo mv ./nginx.conf /etc/nginx/sites-available/bujji-app")
run("sudo ln -sf /etc/nginx/sites-available/bujji-app /etc/nginx/sites-enabled/bujji-app")
run("sudo rm -f /etc/nginx/sites-enabled/default")

run("sudo mkdir -p  /var/www/bujji-app")
run("sudo mv ./index.html /var/www/bujji-app/index.html")

run("sudo nginx -t && sudo systemctl reload nginx")