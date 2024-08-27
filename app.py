# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy product data
products = [
    {
        "id": 1,
        "name": "Product 1",
        "company": "AMZ",
        "category": "Laptop",
        "price": 1500,
        "rating": 4.5,
        "discount": 10,
        "availability": "In Stock",
        "image": "https://via.placeholder.com/150"
    },
    # Add more products
]

# Route to get top N products
@app.route('/http://20.244.56.144/test/companies/:companyname/:categoryname/products?top=n&minPrice=p&maxPrice=q', methods=['GET'])
def get_products():
    top_n = int(request.args.get('top-n', 10))
    min_price = int(request.args.get('minPrice', 0))
    max_price = int(request.args.get('maxPrice', 10000))
    company = request.args.get('company')
    category = request.args.get('category')

    filtered_products = [p for p in products if min_price <= p['price'] <= max_price]

    if company:
        filtered_products = [p for p in filtered_products if p['company'] == company]
    if category:
        filtered_products = [p for p in filtered_products if p['category'] == category]

    return jsonify(filtered_products[:top_n])

if __name__ == '__main__':
    app.run(debug=True)
