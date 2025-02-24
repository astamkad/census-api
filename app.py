from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Census API Key
CENSUS_API_KEY = "046f9c80259c0284cc280f5def016e546222eb15"

# Census API Base URLs
CENSUS_BASE_URL = "https://api.census.gov/data/2020/dec/pl"
CENSUS_BUSINESS_BASE_URL = "https://api.census.gov/data/2020/cbp"
CENSUS_DEMOGRAPHICS_BASE_URL = "https://api.census.gov/data/2021/acs/acs5"

# Route to get list of states
@app.route('/states', methods=['GET'])
def get_states():
    response = requests.get(f"{CENSUS_BASE_URL}?get=NAME&for=state:*&key={CENSUS_API_KEY}")
    if response.status_code == 200:
        data = response.json()
        states = [{"name": state[0], "fips": state[1]} for state in data[1:]]
        return jsonify({"states": states})
    else:
        return jsonify({"error": "Failed to fetch states from U.S. Census API"}), 500

# Route to get list of counties for a given state
@app.route('/counties', methods=['GET'])
def get_counties():
    state_fips = request.args.get('state')
    if not state_fips:
        return jsonify({"error": "Missing state parameter"}), 400

    response = requests.get(f"{CENSUS_BASE_URL}?get=NAME&for=county:*&in=state:{state_fips}&key={CENSUS_API_KEY}")
    if response.status_code == 200:
        data = response.json()
        counties = [{"name": county[0], "fips": county[1]} for county in data[1:]]
        return jsonify({"counties": counties})
    else:
        return jsonify({"error": "Failed to fetch counties from U.S. Census API"}), 500

# Route to get business data for a county
@app.route('/businesses', methods=['GET'])
def get_businesses():
    state_fips = request.args.get('state')
    county_fips = request.args.get('county')

    if not state_fips or not county_fips:
        return jsonify({"error": "Missing state or county parameter"}), 400

    response = requests.get(
        f"{CENSUS_BUSINESS_BASE_URL}?get=NAICS2017_LABEL,ESTAB&for=county:{county_fips}&in=state:{state_fips}&key={CENSUS_API_KEY}"
    )

    if response.status_code == 200:
        data = response.json()
        businesses = [{"industry": entry[0], "establishments": entry[1]} for entry in data[1:]]
        return jsonify({"businesses": businesses})
    else:
        return jsonify({"error": "Failed to fetch business data from U.S. Census API"}), 500

# Route to get ZIP Code-level demographic data
@app.route('/zip-demographics', methods=['GET'])
def get_zip_demographics():
    zcta = request.args.get('zip')

    if not zcta:
        return jsonify({"error": "Missing ZIP code parameter"}), 400

    response = requests.get(
        f"{CENSUS_DEMOGRAPHICS_BASE_URL}?get=NAME,B01003_001E,B25001_001E&for=zip code tabulation area:{zcta}&key={CENSUS_API_KEY}"
    )

    if response.status_code == 200:
        data = response.json()
        demographics = {
            "zip": data[1][0],
            "population": data[1][1],
            "housing_units": data[1][2]
        }
        return jsonify({"demographics": demographics})
    else:
        return jsonify({"error": "Failed to fetch ZIP code demographics from U.S. Census API"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
