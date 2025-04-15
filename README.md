# 🚌 CityBus Dashboard

A professional, interactive dashboard built with **Streamlit** and **Plotly** to visualize and analyze monthly public transit data. Designed for transit authorities, researchers, or civic tech teams to track route performance and efficiency.

Link to the app --> https://citybus-dashboard.streamlit.app/

---

## 🔧 Features

- Upload one or more **monthly CSV reports**
- Visualizes key metrics for each route:
  - 📊 Total Passengers per Route
  - 💰 Total Revenue per Route
  - 🚍 Passengers per Mile (Efficiency)
  - ⏱️ Passengers per Hour (Efficiency)
  - 📈 Monthly Passenger Trends
  - 🔁 Revenue vs. Passenger Correlation
- Supports multi-month uploads with automatic aggregation
- Fully interactive visuals powered by **Plotly**

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<YOUR_USERNAME>/citybus-dashboard.git
cd citybus-dashboard
```

### 2. Install dependencies
Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

---

## 📂 File Structure

```
citybus-dashboard/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 📊 Sample Input

The app expects CSV files with fields like:

- `RouteName`
- `Passengers`
- `Revenue`
- `Total Miles`
- `Total Hours`

Each file should represent **one month**. You'll be prompted to enter the corresponding month when uploading.

---

## 📝 License

This project is open source under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Built by Archer, Eli, and Mabel — feel free to reach out or contribute!
```
