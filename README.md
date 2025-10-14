#  Mini Python Projects

Welcome to the **Mini Python Projects** repository – a curated collection of beginner-friendly Python projects designed to enhance your coding skills through hands-on practice. Whether you're new to Python or looking to build small utility-based apps, this repository is a great place to start.

---

### 1. QR Code Generator
A simple tool to generate QR codes for URLs or text using Python.

- **Folder**: `QR_Code_Generator`  
- **Libraries Used**: `qrcode`  
- **Features**:
  - Generate custom QR codes  
  - Save as PNG images  
  - Customize size and colors  

---

### 2. PDF Merger
Merge multiple PDF files into one using a clean and interactive Jupyter Notebook interface.

- **Folder**: `pdf-merger`  
- **Libraries Used**: `PyPDF2`  
- **Features**:
  - Select multiple PDFs  
  - Output a single combined PDF  
  - Simple and efficient  

---

### 3. Handwritten Text Generator
Convert typed text into realistic-looking handwritten images using a custom handwriting font.

- **Folder**: `handwritten-text-generator`  
- **Libraries Used**: `Pillow (PIL)`  
- **Features**:
  - Input any custom text  
  - Generate a PNG image in a handwritten style  
  - Supports multi-line and wrapped text  
  - Uses `.ttf` font like `Pacifico-Regular.ttf` for handwriting effect  

---

### 4. Yahoo Finance – Multi-Stock Price Scraper
Fetch historical price data for several stocks from Yahoo Finance and save everything into a single CSV file.  
Great starting point for ML projects like return prediction, portfolio analysis, or risk studies.

- **Folder**: `Yahoo_finance`  
- **Libraries Used**: `yfinance`, `pandas`  
- **Features**:
  - Download OHLCV data (Open, High, Low, Close, Volume, Adj Close) for multiple tickers  
  - Store results in a single CSV with a `Ticker` column  
  - Clean, ready-to-use dataset for analytics or machine learning  

---

### 5. Weather App
A simple Python tool that fetches live weather information (temperature, humidity, and condition) for any city using the OpenWeatherMap API.

- **Folder**: `weather_app`  
- **Libraries Used**: `requests`  
- **API Used**: [OpenWeatherMap API](https://openweathermap.org/api)  
- **Features**:
  - Fetch real-time weather data by city name  
  - Displays temperature, humidity, pressure, and condition  
  - Uses a free API key and handles invalid city errors  

---

#### Installation
```bash
pip install qrcode PyPDF2 Pillow yfinance pandas requests
```
