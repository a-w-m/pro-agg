from flask import Flask

app = Flask(__name__, static_url_path='/', static_folder="../client/dist")

from application import routes