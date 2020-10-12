from application import app
from flask import jsonify
from application.soup.jacobin import jacobin
from application.soup.baffler import baffler
from application.soup.truthout import truthout
from application.soup.viewpoint import viewpoint
from application.soup.roarmag import roarmag


@app.route("/api", methods = ['GET'])

def index():
    response = jsonify(jacobin = jacobin, baffler = baffler, truthout = truthout, viewpoint = viewpoint, roarmag = roarmag)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response