import requests

# Importación:
# - requests: para enviar solicitudes HTTP al endpoint de predicción


url = 'http://localhost:9696/predict'

# Definición de un cliente de prueba con sus características
customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

# Enviar la solicitud POST al endpoint con los datos del cliente
response = requests.post(url, json=customer)

# Obtener la respuesta en formato JSON
predictions = response.json()

# Uso de la predicción en lógica de negocio
if predictions['churn']:
    print('customer is likely to churn, send promo')
else:
    print('customer is not likely to churn')
