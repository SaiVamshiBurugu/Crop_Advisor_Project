# 🌾 Crop Recommendation System using Machine Learning and Streamlit

An interactive web application that predicts the **best crop to grow** based on soil and environmental conditions.  
This project integrates a **Random Forest Machine Learning model** with a **Streamlit web interface**, providing farmers, researchers, and agricultural planners with data-driven crop recommendations.

Check the App Here: https://cropadvisorproject-mg3y6edds6bymnannfvaml.streamlit.app/
---

## 📘 Overview

- Built and trained a **Random Forest Classifier** on the **Crop Recommendation Dataset**.
- Integrated the trained ML model with **Streamlit** for real-time predictions.
- Achieved **99.39% accuracy** on the test dataset.
- Designed an intuitive **web interface** where users can input environmental factors to get the best crop recommendation.

---

## 🧠 Machine Learning Pipeline

1. **Data Preprocessing**
   - Loaded and cleaned dataset using `pandas`.
   - Scaled features using `StandardScaler`.
   - Encoded crop labels using `LabelEncoder`.

2. **Model Training**
   - Trained a `RandomForestClassifier` on processed data.
   - Tuned model parameters to maximise accuracy.

3. **Evaluation**
   - Achieved **99.39% accuracy** on test data.
   - Verified model using accuracy metrics and visualisations.

4. **Deployment**
   - Built an interactive **Streamlit web app** (`app.py`).
   - Integrated trained model and label encoder using `joblib`.

---

## 🧩 Dataset Information

| Feature | Description |
|----------|-------------|
| N | Ratio of Nitrogen content in soil |
| P | Ratio of Phosphorus content in soil |
| K | Ratio of Potassium content in soil |
| temperature | Temperature (°C) |
| humidity | Relative humidity (%) |
| ph | pH value of the soil |
| rainfall | Rainfall in mm |
| label | Recommended crop name |

---

## 📈 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | **99.39%** |
| Model | Random Forest Classifier |
| Scaler | StandardScaler |
| Encoder | LabelEncoder |

---

## 💻 Streamlit Web App

### 🎯 Features
- Simple, interactive form to input environmental parameters.
- Displays the **predicted crop name instantly**.
- Clean and responsive UI built with Streamlit components.

### 🚀 To Run Locally

```bash
# Clone the repository
git clone https://github.com/SaiVamshiBurugu/Crop_Advisor_Project.git

# Navigate to the project directory
cd Crop_Recommendation_System

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```




