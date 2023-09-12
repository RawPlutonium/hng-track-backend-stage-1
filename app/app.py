import requests
import datetime
import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def api():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    current_day = datetime.datetime.now().strftime("%A")
    utc_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

    github_file_url = requests.get(
        "https://api.github.com/repos/rawplutonium/hng-track-backend-stage-1/commits/HEAD"
    ).json()["url"]
    github_repo_url = "https://github.com/rawplutonium/hng-track-backend-stage-1"

    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }

    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=False)
