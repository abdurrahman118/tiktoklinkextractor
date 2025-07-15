@app.route("/get-links", methods=["POST"])
def api_get_links():
    try:
        username = request.form["username"].replace("@", "").strip()
        if not username:
            return jsonify({"error": "Username cannot be empty"}), 400
            
        # Replace this with real TikTok API calls
        links = [
            f"https://www.tiktok.com/@{username}/video/7268028301785206021",
            f"https://www.tiktok.com/@{username}/video/7268028301785206022"
        ]
        
        return jsonify({"links": links})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
