from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    recommendations = [
        {"item": "Product A", "action": "Restock"},
        {"item": "Product B", "action": "Promote Discount"}
    ]
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)