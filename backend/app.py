from flask import Flask, request, jsonify
from flask_cors import CORS
from news_checker import check_news_validity

app = Flask(__name__)
CORS(app)


# 🔍 Endpoint 1: /verify_news
# Purpose: Accept news data and validate it using your AI logic.
@app.route('/verify_news', methods=['POST'])
def verify_news():
    data = request.json
    result = check_news_validity(data)  # Calls your fake AI logic
    return jsonify(result)

# 🔗 Endpoint 2: /trigger_fund
# Purpose: Trigger smart contract to release funds (you’ll integrate Web3.py here).
@app.route('/trigger_fund', methods=['POST'])
def trigger():
    # TODO: Add smart contract trigger logic here
    return jsonify({"status": "Funds Released", "txn": "0xabc123..."})

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
