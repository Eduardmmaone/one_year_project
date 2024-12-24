# one_year_project

# Прогнозирование оттока клиентов

Этот проект демонстрирует полный цикл прогнозирования оттока клиентов с использованием методов машинного обучения. Цикл включает предварительную обработку данных, обучение модели, настройку гиперпараметров, оценку модели и развертывание с использованием Flask. В проекте также используется MLflow для отслеживания экспериментов и версионирования моделей.

---

## Возможности

- **Предварительная обработка данных**: Работа с дисбалансом классов (SMOTE и ADASYN), отбор признаков и масштабирование.
- **Обучение модели**: Реализация моделей LightGBM и XGBoost с настройкой гиперпараметров.
- **Отслеживание экспериментов**: Использование MLflow для логирования параметров, метрик и моделей.
- **Развертывание модели**: Развертывание RESTful API с использованием Flask.

---

## Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/yourusername/customer-churn-prediction.git
   cd customer-churn-prediction
   ```

2. **Создайте виртуальное окружение**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # В Windows: venv\Scripts\activate
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте MLflow** (если требуется):
   Запустите MLflow UI для отслеживания экспериментов:
   ```bash
   mlflow ui
   ```
   Интерфейс будет доступен по адресу: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Использование

### 1. Обучение модели

Запустите скрипт для обработки данных, обучения модели и логирования лучшей модели в MLflow:
```bash
python train_model.py
```

### 2. Запуск Flask-сервера

Измените файл сервера Flask (`flask_server.py`), чтобы загрузить нужную модель из MLflow:
```python
logged_model = 'runs:/<run_id>/model'
```

Запустите Flask-сервер:
```bash
python flask_server.py
```

Сервер будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 3. Тестирование API

Отправьте POST-запрос на эндпоинт `/predict` с данными клиента:
```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"CreditScore": 600, "Age": 40, "Balance": 50000, "NumOfProducts": 2, "IsActiveMember": 1, "Geography_Germany": 0, "Geography_Spain": 1, "Gender_Male": 1}'
```
Ожидаемый ответ:
```json
{
    "prediction": 1,
    "probability": 0.7714658351089848
}
```


## Требования

- Python 3.7+
- MLflow
- Flask
- LightGBM
- XGBoost


