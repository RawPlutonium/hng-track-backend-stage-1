import datetime
import json
from flask import Flask, request, jsonify  # Import jsonify for setting the content type
import requests

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def api():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    # Get the current UTC time in the specified format
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Fetch the GitHub commit URL
    github_file_url = "https://api.github.com/repos/rawplutonium/hng-track-backend-stage-1/commits/HEAD"
    try:
        response = requests.get(github_file_url)
        response.raise_for_status()
        github_data = response.json()
        github_file_url = github_data.get("html_url")
    except requests.exceptions.RequestException as e:
        return json.dumps({"error": "Failed to fetch GitHub data"}), 500

    # Construct the response JSON as specified
    data = {
        "slack_name": slack_name,
        "current_day": datetime.datetime.now().strftime("%A"),
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": "https://github.com/rawplutonium/hng-track-backend-stage-1",
        "status_code": 200,
    }

    # Set the content type to "application/json"
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=False)
