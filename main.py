import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import openai

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate-image", methods=["POST"])
def generate_image():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Brak promptu"}), 400

        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )

        image_url = response['data'][0]['url']

        return jsonify({
            "finalPrompt": prompt,
            "imageUrl": image_url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
