from flask import Flask, request, jsonify
import mlflow.sklearn
import numpy as np

# Инициализация Flask-приложения
app = Flask(__name__)

# Укажите путь к модели в MLflow
logged_model = 'runs:/89cb61a6b0aa4a2987e8183975814582/lightgbm_model' 

# Загрузка модели из MLflow
model = mlflow.sklearn.load_model(logged_model)

@app.route('/predict', methods=['POST'])
def predict():
    # Получение данных из запроса
    data = request.json
    
    # Преобразование данных в массив numpy
    input_data = np.array([data[feature] for feature in model.feature_name_]).reshape(1, -1)
    
    # Предсказание
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0, 1]
    
    # Возврат результата
    return jsonify({
        'prediction': int(prediction[0]),
        'probability': float(probability)
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000)

