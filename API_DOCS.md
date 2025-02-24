# Easely Census API Documentation

## **Overview**
The Easely Census API provides access to business, demographic, and geographic data using the U.S. Census Bureau API. The API includes endpoints for retrieving U.S. states, counties, business establishments, and ZIP code demographics.

## **Base URL**
https://easely-census-api.onrender.com

---

## **📌 Endpoints & Usage**

### **1️⃣ Get List of U.S. States**
- **Endpoint:** `/states`
- **Method:** `GET`
- **Description:** Returns a list of all U.S. states with their **FIPS codes**.
- **Example Request:** curl -X GET “https://easely-census-api.onrender.com/states”

- **Example Response:**
```json
{
  "states": [
    {"fips": "42", "name": "Pennsylvania"},
    {"fips": "06", "name": "California"},
    {"fips": "54", "name": "West Virginia"}
  ]
}

### **2️⃣ Get Counties in a State
	•	Endpoint: /counties
	•	Method: GET
	•	Description: Fetches all counties within a given state.
	•	Query Parameters:
	•	state (Required) → FIPS code of the state.
	•	Example Request: curl -X GET "https://easely-census-api.onrender.com/counties?state=06"
  •	Example Response:
  {
  "counties": [
    {"fips": "075", "name": "San Francisco County, California"},
    {"fips": "037", "name": "Los Angeles County, California"}
  ]
}

Yes, you can create the file in Atom inside your easely-census-api directory. The best practice is to name it API_DOCS.md (Markdown file).

Here’s how to create it in Atom:
	1.	Open Atom and navigate to your easely-census-api directory.
	2.	Click File → New File.
	3.	Save it as API_DOCS.md inside the easely-census-api directory.
	4.	Copy and paste the following API documentation into it.

📄 Easely Census API Documentation

# Easely Census API Documentation

## **Overview**
The Easely Census API provides access to business, demographic, and geographic data using the U.S. Census Bureau API. The API includes endpoints for retrieving U.S. states, counties, business establishments, and ZIP code demographics.

## **Base URL**

https://easely-census-api.onrender.com

---

## **📌 Endpoints & Usage**

### **1️⃣ Get List of U.S. States**
- **Endpoint:** `/states`
- **Method:** `GET`
- **Description:** Returns a list of all U.S. states with their **FIPS codes**.
- **Example Request:**

curl -X GET “https://easely-census-api.onrender.com/states”

- **Example Response:**
```json
{
  "states": [
    {"fips": "42", "name": "Pennsylvania"},
    {"fips": "06", "name": "California"},
    {"fips": "54", "name": "West Virginia"}
  ]
}

2️⃣ Get Counties in a State
	•	Endpoint: /counties
	•	Method: GET
	•	Description: Fetches all counties within a given state.
	•	Query Parameters:
	•	state (Required) → FIPS code of the state.
	•	Example Request:

curl -X GET "https://easely-census-api.onrender.com/counties?state=06"


	•	Example Response:

{
  "counties": [
    {"fips": "075", "name": "San Francisco County, California"},
    {"fips": "037", "name": "Los Angeles County, California"}
  ]
}

3️⃣ Get Business Data by County
	•	Endpoint: /businesses
	•	Method: GET
	•	Description: Returns the number of business establishments in a county.
	•	Query Parameters:
	•	state (Required) → FIPS code of the state.
	•	county (Required) → FIPS code of the county.
	•	Example Request:

curl -X GET "https://easely-census-api.onrender.com/businesses?state=06&county=075"


	•	Example Response:

{
  "businesses": [
    {"industry": "Total for all sectors", "establishments": "34692"}
  ]
}


4️⃣ Get ZIP Code Demographics
	•	Endpoint: /zip-demographics
	•	Method: GET
	•	Description: Returns population and housing unit data for a given ZIP code.
	•	Query Parameters:
	•	zip (Required) → 5-digit ZIP code.
	•	Example Request:

curl -X GET "https://easely-census-api.onrender.com/zip-demographics?zip=94102"


	•	Example Response:

{
  "demographics": {
    "zip": "ZCTA5 94102",
    "population": "33856",
    "housing_units": "22272"
  }
}



💡 Notes
	•	Ensure you provide the correct FIPS codes for states and counties.
	•	ZIP code demographics are based on ZCTA5 codes from the U.S. Census Bureau.
	•	The API sources data from the 2020 Census and 2020 County Business Patterns datasets.
	•	If an invalid request is made, an error message will be returned.

📩 Support

For questions, reach out via GitHub issues or contact the Easely development team.
