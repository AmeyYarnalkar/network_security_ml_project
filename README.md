# Phishing Website Detection (ML + Web App)

A simple end-to-end machine learning project that detects whether a website is legitimate or phishing.

You can:

* Enter a URL and get instant prediction
* Upload a CSV file for batch prediction

---

## How it works (simple view)

1. Take a URL or CSV input
2. Extract features from the URL
3. Run a trained ML model
4. Return prediction

---

## Model Training

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python main.py
```

This will:

* Perform ETL (read raw data, convert to JSON, and store in MongoDB Atlas)
* Run data ingestion
* Perform data validation
* Run data transformation
* Train the model
* Save the trained model

---

## Run Web Application

To start the web app:

```bash
python app.py
```

Then open in browser:

```text
http://localhost:8080
```

---

## Features Used

The model uses features extracted from:

### URL structure

Examples:

* Length of URL
* Presence of `@`
* Number of subdomains
* Use of IP address instead of domain

### Basic HTML signals

Examples:

* External links
* Forms
* Redirect behavior

---

## Important Note

* Feature extraction is based on URL structure and basic HTML parsing only
* Some features (like traffic, ranking, etc.) are not fetched dynamically

Default values are used for those features to keep the system simple, fast, and reliable.

---

## Project Design

This project follows a modular structure and simulates a simple production workflow.

It includes:

* ETL process (raw data → JSON → MongoDB Atlas)
* Data ingestion
* Data validation
* Data transformation
* Model training

---

## Additional Implementation Details

* Custom logging system for tracking pipeline execution
* Custom exception handling for better debugging
* Raw feature extraction pipeline for URL inputs
* Clean separation of components inside `src/`

---

## Project Structure

```text
src/
  components/
  pipeline/
  utils/
  logging/
  exceptions/

Data/
notebooks/
schema/
Dockerfile
requirements.txt
app.py
main.py
```

---

## Run with Docker (optional)

```bash
docker build -t phishing-detector .
docker run -p 8080:8080 phishing-detector
```

---

## What this project shows

* End-to-end ML pipeline
* Feature engineering from real inputs
* ETL and data validation workflow
* Web app integration
* Docker-based deployment
* Cloud-ready system

---

## Future Improvements

* Better feature extraction using live data sources
* Improve model accuracy
* Add API endpoints
* Add rate limiting and security

---

Built as a practical ML + deployment project with a focus on clean structure and real-world workflow.
