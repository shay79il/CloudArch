from flask import Flask, json, request

pizza_type = ["napolitana", "salami", "pork", "pinapple"]
pizza_size = ["personal", "family"]
pizza_orders = [
  {"pizza": "pork", "size": "personal", "amount": 21}
]

app = Flask("PizzaOrder")

@app.route('/order', methods=['POST'])
def order_pizza():
  if request.method == 'POST':
    request_data = request.get_json()
    pizza_orders.append(request_data)
    return {'Pizza': request_data['pizza'], 'completed': True, 'return': 200}

@app.route('/ping', methods=['GET'])
def my_ping():
  return {'ping': True, 'return': 200}

@app.route('/health', methods=['GET'])
def health():
  return {'AppHealthy': True, 'return': 200}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)