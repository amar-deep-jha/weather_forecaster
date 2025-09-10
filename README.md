# 🌦️ Weather API Client (Python)

A simple Python project to fetch **real-time weather data** for any city using the **OpenWeatherMap API**.  
This project is part of **Month 2: Intermediate Python Concepts** (Functions, Exception Handling, APIs).  

---

## 📌 Features
- Fetches live weather data (temperature, condition, location).  
- Uses **functions** to keep code modular and reusable.  
- Implements **exception handling** for:
  - Invalid city names
  - Network errors
  - Invalid or missing API key  
- Uses Python’s **requests** library to call APIs.  

---

## 🚀 Setup Instructions

### 1. Clone / Download the Project
```bash
git clone https://github.com/your-username/weather-api-client.git
cd weather-api-client
```

### 2. Install Dependencies
Make sure you have Python 3.10+ installed. Then install `requests`:
```bash
pip install requests
```

### 3. Get Your Free API Key
- Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)  
- Sign up and confirm your email.  
- Copy your API key from **My API Keys**.  
- ⚠️ Keys may take up to **15 minutes** to activate.  

### 4. Update Your API Key
Open `weather_api.py` and replace:
```python
api_key = "YOUR_API_KEY"
```
with your actual key:
```python
api_key = "your_real_api_key_here"
```

---

## ▶️ Usage
Run the script from terminal:
```bash
python weather_api.py
```

Example:
```
Enter city name: Kanpur
Request completed.
🌍 Kanpur, IN
🌡️ Temp: 31°C
☁️ Weather: haze
```

---

## ⚡ Error Handling
- Invalid City → `⚠️ API Error: city not found`  
- Wrong API Key → `⚠️ API Error: Invalid API key`  
- No Internet → `⚠️ Network/Request error: ...`  

---

## 📚 Concepts Practiced
- **Functions & Modular Code** – reusable function to fetch weather.  
- **Exception Handling** – try/except/finally blocks.  
- **APIs & JSON** – used OpenWeatherMap REST API.  

---

## 🛠️ Future Improvements
- Add forecast data (5-day weather).  
- Save results in a file (`weather_log.txt`).  
- Build a GUI version with Tkinter or Flask.  

---

## 📄 License
This project is for educational purposes (Internship / Training). Free to use and modify.  
