from flask import Flask, jsonify
import requests

app = Flask(__name__)

# U.S. Census API Configuration
CENSUS_API_BASE = "https://api.census.gov/data"
CENSUS_YEAR = "2020"
DATASET = "dec/pl"  # Correct dataset
CENSUS_API_KEY = "046f9c80259c0284cc280f5def016e546222eb15"  # Your API Key

@app.route("/states", methods=["GET"])
def get_states():
    """Fetch all U.S. states with their FIPS codes from the Census API."""
    url = f"{CENSUS_API_BASE}/{CENSUS_YEAR}/{DATASET}?get=NAME&for=state:*&key={CENSUS_API_KEY}"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({
                "error": "Failed to fetch states from U.S. Census API",
                "status_code": response.status_code,
                "details": response.text
            }), 500

        data = response.json()
        states = [{"name": item[0], "fips": item[1]} for item in data[1:]]  # Skip header row
        return jsonify({"states": states})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
