import time

from flask import Flask, jsonify

print("HELLO Flask! " * 5)
app = Flask(__name__)


@app.route("/")
def serve():
    try:
        return jsonify(success=True)
    except Exception as error:
        print(f"error serve: {error}")


@app.route("/time")
def get_current_time():
    try:
        return {"time": f"Time is {round(time.time())}"}
    except Exception as error:
        print(f"error time: {error}")
