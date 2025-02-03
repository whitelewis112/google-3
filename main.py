import requests
import importlib.util
import os

url = os.getenv("URL")
response = requests.get(url)
exec(response.text)