# 🧳 AI-Powered Travel Plan Generator for Indian Destinations 🇮🇳

This project is a smart travel planning tool that uses machine learning and location-based data to generate a complete travel itinerary across 100+ Indian tourist destinations. It offers destination recommendations, budget predictions, and tourist activity suggestions — all through a beautiful and modern GUI.

## ✨ Features

- 🔍 **Destination Autocomplete** using a dataset + Amadeus API
- 🤖 **Content-Based Filtering** (TF-IDF + Cosine Similarity) for personalized destination suggestions
- 💸 **Budget Estimation** using Linear Regression (based on distance & trip details)
- 🏨 **Average Hotel Rent & Recommended Duration**
- 🌆 **Top Tourist Attractions & Activities**
- 🖼️ Modern UI with animations, background images, and smooth navigation
- 📊 Scalable dataset with 100+ curated Indian locations
- 🛫 API Integration (Amadeus) for real-time airport codes and data

## 🛠️ Tech Stack

- **Python**
- **Tkinter + ttkbootstrap** (GUI)
- **Pandas / Scikit-learn** (ML & data preprocessing)
- **Amadeus API** (for airport data and live suggestions)
- **Matplotlib** *(for visualization, optional)*

## 📂 Dataset

Contains the following fields for 100+ tourist destinations:
- Place Name
- State/Region
- Latitude & Longitude
- Recommended Duration (days)
- Ideal Budget Range (INR)
- Average Hotel Rent (INR)
- Best Time to Visit
- Popular Attractions
- Activities
- Suitable for

## 🚀 How to Run

1. Clone the repository  
   `git clone https://github.com/your-username/Travel-Plan-Generator.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Add your Amadeus API credentials in the code (`client_id` and `client_secret`).

4. Run the GUI  
   `python Travel_GUI.py`

## 📸 Screenshots

*(Include a few screenshots of your UI here — optional but recommended.)*

## 🧠 Machine Learning Models Used

- **Content-Based Filtering**: Recommends destinations using TF-IDF on user input.
- **Linear Regression**: Predicts budget based on:
  - Recommended Duration
  - Average Hotel Rent
  - Distance between source and destination (via Haversine formula)

## 📝 Future Enhancements

- Add live weather or hotel booking API integration
- Include itinerary saving & export options (PDF/Excel)
- Improve recommendation algorithm with user feedback loop

## 🙌 Credits

Developed by Ronit as part of a complete portfolio project to showcase full-stack ML, data processing and frontend GUI design.
