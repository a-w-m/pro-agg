from application import app
from flask import jsonify
from application.soup.jacobin import run_jacobin
from application.soup.baffler import run_baffler
from application.soup.roarmag import run_roarmag
from application.soup.truthout import run_truthout
from application.soup.viewpoint import run_viewpoint



@app.route("/api", methods = ['GET'])

def index():
    response = jsonify(jacobin = run_jacobin(), baffler = run_baffler(), truthout = run_truthout(), roarmag = run_roarmag(), viewpoint = run_viewpoint())
    return response