import logging
import sys

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Web App with Python Flask!"


@app.route("/cpu", methods=["GET"])
def cpu_test():

    res = 0
    for i in range(1000):
        res = res + 1

    return f"This is function use high cpu : {res}"


@app.route("/ram", methods=["GET"])
def ram_test():

    res = [0]
    for i in range(100):
        res = [0] * i

    return f"This is function suse high ram : {res}"


@app.route("/pizza-bug", methods=["POST"])
def make_bugs():
    slices = 12

    nbr_guests = request.json["guests"]

    try:
        return f"There will be {slices / nbr_guests} slices each"
    except:
        return "This is a bad practice :) "


if __name__ == "__main__":
    try:
        # Setup a logger for debugpy to print into stdout
        debugpy_logger = logging.getLogger("debugpy")
        debugpy_logger.setLevel(logging.DEBUG)
        stdout_handler = logging.StreamHandler(sys.stdout)
        debugpy_logger.addHandler(stdout_handler)

        debugpy_logger.debug("🐞 debugpy - Importing module...")
        import debugpy

        debugpy.log_to("/tmp/debugpy")
        debugpy_logger.debug("🐞 debugpy - Printing logs to `/tmp/debugpy`...")

        debugpy.listen(("0.0.0.0", 5678))
        debugpy_logger.debug("🐞 debugpy - Listening at 0.0.0.0:5678...")

    except RuntimeError:
        debugpy_logger.debug(
            "🐞 debugpy - Got Runtime error. Ignore if running in Flask."
        )

    # Create the debug mode app
    app.run(host="0.0.0.0", port=5000)
