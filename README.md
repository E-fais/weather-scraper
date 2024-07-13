# Doha Weather App

A simple Python script to scrape hourly weather data for Doha from AccuWeather and save it to a CSV file.

## Requirements

- requests
- BeautifulSoup4
- pandas

## Usage

1. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

2. Run the script:
   ```bash
   python app.py
   ```

3. The script will print the maximum and minimum temperatures and save the weather data to `weather.csv`.

## Description

The script performs the following steps:
- Sends a GET request to AccuWeather for Doha's hourly weather.
- Parses the HTML content using BeautifulSoup.
- Extracts time and temperature data.
- Saves the data to `weather.csv`.
- Prints the minimum and maximum temperatures.
```
