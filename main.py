from flask import Flask, render_template, request, jsonify
import requests  # For TikTok API calls

app = Flask(__name__)

# Mock function (replace with real TikTok API)
def get_tiktok_video_links(username):
    # Simulate API delay
    import time
    time.sleep(2)

    # Mock data for demo
    return [
        f"https://www.tiktok.com/@{username}/video/7268028301785206021",
        f"https://www.tiktok.com/@{username}/video/7268028301785206022",
        f"https://www.tiktok.com/@{username}/video/7268028301785206023",
    ]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-links", methods=["POST"])
def api_get_links():
    username = request.form["username"].replace("@", "")
    links = get_tiktok_video_links(username)
    return jsonify({"links": links})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
