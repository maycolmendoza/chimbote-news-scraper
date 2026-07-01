import os
import requests

url = os.getenv("APPS_SCRIPT_URL")

requests.post(
    url,
    json={
        "mensaje":"Hola desde GitHub"
    }
)

print("Enviado")
