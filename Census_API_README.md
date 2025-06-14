
# 🗺️ Census API for Business Insights

This API provides structured access to U.S. Census Bureau data, including demographic and business data by **state**, **county**, and **ZIP code**. It was developed to support projects like [Xuno](https://assorted-organ-be9.notion.site/Asta-Musa-Portfolio-212011f7ce1c80aeb0c7f49798a04bbe), which deliver market insights to small businesses operating in underserved regions.

---

## 🚀 Features

- Retrieve list of all U.S. states and counties
- Access business establishment counts by county
- Fetch ZIP code-level population and household statistics
- Clean, lightweight Flask-based implementation

---

## 📦 Endpoints

### `GET /states`
Returns a list of U.S. states with FIPS codes.

### `GET /counties/{state_fips}`
Returns counties within a given state using its FIPS code.

### `GET /businesses/{state}/{county}`
Returns business establishment data for a specific county.

### `GET /zipcode/{zipcode}`
Returns population and household data by ZIP code.

---

## 🛠️ Technologies Used

- Python 3.10
- Flask
- U.S. Census Bureau APIs
- Render (for deployment)

---

## 🧠 Use Case

Originally designed for use in **Xuno**, this API supports small business owners by providing hyperlocal demographic and economic data to inform:
- Market research
- Location planning
- Community-level strategy

---

## 👩🏾‍💻 Author

Developed by **Asta Musa**  
LinkedIn | [Portfolio](https://assorted-organ-be9.notion.site/Asta-Musa-Portfolio-212011f7ce1c80aeb0c7f49798a04bbe)

---

## 📜 License

MIT License
