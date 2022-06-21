from cProfile import run
from application import app
from flask import jsonify
import schedule, time, threading
from application.soup.jacobin import run_jacobin
from application.soup.baffler import run_baffler
from application.soup.roarmag import run_roarmag
from application.soup.truthout import run_truthout
from application.soup.viewpoint import run_viewpoint


def combine_soup():
    return {
        "jacobin": run_jacobin(),
        "baffler": run_baffler(),
        "truthout": run_truthout(),
        "roarmag": run_roarmag(),
        "viewpoint": run_viewpoint()
    }


combined_soup = combine_soup()


def sched_soup():
    global combined_soup
    combined_soup = combine_soup()


def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.daemon = True
    job_thread.start()


schedule.every(12).hours.do(run_threaded, sched_soup)
run_threaded(run_schedule)


@app.route("/", methods=["GET"])
def index():
    return app.send_static_file("index.html")


@app.route("/api", methods=["GET"])
def api():
    global combined_soup
    return jsonify(combined_soup)
