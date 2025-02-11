
# Cardiovascular Disease Prediction

This project focuses on predicting the risk of cardiovascular diseases using machine learning techniques. The goal is to implement data preprocessing, feature engineering, and model selection to achieve accurate predictions.

## Project Overview

Cardiovascular diseases (CVDs) are a leading cause of mortality globally. Early detection through predictive modeling can aid in timely intervention and treatment. This project explores various machine learning models to predict the likelihood of CVDs based on patient data.

## Dataset

The dataset used in this project contains various health indicators related to cardiovascular health. It includes features such as age, gender, blood pressure, cholesterol levels, and more.

## Methodology

1. **Data Preprocessing**: Handled missing values, normalized numerical features, and encoded categorical variables.

2. **Feature Engineering**: Created new features and selected the most relevant ones to improve model performance.

3. **Model Selection**: Compared multiple machine learning algorithms, including K-Nearest Neighbors (KNN), to identify the most effective model.

4. **Model Evaluation**: Assessed models using metrics such as accuracy, precision, recall, and F1-score.

## Results

The KNN model demonstrated promising results in predicting cardiovascular disease risk. The trained model is saved as `knn_production_model.joblib` for future use.

## Repository Contents

- `diseas_model.ipynb`: Jupyter Notebook containing the full analysis and model development process.

- `production_model.py`: Script for deploying the trained model.

- `knn_production_model.joblib`: Serialized KNN model for prediction tasks.

- `test_sample.csv`: Sample data for testing the model.

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/koop46/ML_cardio_diseas_prediction.git
   cd ML_cardio_diseas_prediction
   ```

2. **Install Dependencies**:

   Ensure you have the necessary Python libraries installed, such as `pandas`, `numpy`, `scikit-learn`, and `joblib`.

3. **Run the Notebook**:

   Open and execute `diseas_model.ipynb` to see the data analysis and model training steps.

4. **Model Deployment**:

   Use `production_model.py` to load the trained model and make predictions on new data.

## Conclusion

This project highlights the application of machine learning in healthcare, specifically in predicting cardiovascular disease risk. The methodologies and results demonstrate the potential for data-driven approaches to support early diagnosis and intervention.

---

Feel free to customize these descriptions further to align with your specific experiences and the requirements of the internship you're applying for. 
