import pickle
import numpy as np
from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    print("Error: 'model.pkl' not found. Please ensure the model file is in the correct directory.")
    model = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

scaler = StandardScaler()
n_cols = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']
pssl = np.random.rand(10, len(n_cols))
scaler.fit(pssl)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction_text='Model not loaded. Please check the server logs.')

    try:
        features = [float(x) for x in request.form.values()]
        f_f = np.array(features).reshape(1, -1)
        scaled_features = f_f.copy()
        n_indices = [0, 2, 4, 6, 7, 8, 11] 
    
        num_d = scaled_features[0, n_indices].reshape(1, -1)
        scaled_numerical_data = scaler.transform(num_d)
        scaled_features[0, n_indices] = scaled_numerical_data

        prediction = model.predict(scaled_features)

        if prediction[0] == 1:
            output = "A Death event is likely."
        else:
            output = "The patient is likely to Survive."

        return render_template('index.html', prediction_text=f'Prediction: {output}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error during prediction: {e}')


if __name__ == "__main__":
    app.run(debug=True)
