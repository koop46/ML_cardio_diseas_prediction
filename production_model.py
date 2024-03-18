import pandas as pd
import joblib


knn_model = joblib.load('knn_production_model.joblib')
sample_df = pd.read_csv('test_sample.csv')

sample_X, sample_y = sample_df.drop(['id', 'bmi', 'bp_category', 'height_cm', 'weight_kg', 'cardio_diseas'], axis='columns'), sample_df['cardio_diseas']
sample_X = pd.get_dummies(sample_X, columns = ['gender'], dtype=int)

model_prediction = knn_model.predict(sample_X)
probabilities = knn_model.predict_proba(sample_X)


df = pd.DataFrame(probabilities)
df['predictions'] = model_prediction
df.columns = ['probabilitiy_class_0', 'probabilitiy_class_1', 'prediction']

df.to_csv('prediction.csv', index=False)  
print(df)


