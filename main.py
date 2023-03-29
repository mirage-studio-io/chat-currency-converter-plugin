import os
import quart
import quart_cors
from quart import Quart, jsonify, request

PORT = 5002
CONVERSION_RATES = {
  "USD": {
    "EUR": 0.85,
    "JPY": 110.0
  },
  "EUR": {
    "USD": 1.18,
    "JPY": 129.0
  },
  "JPY": {
    "USD": 0.0091,
    "EUR": 0.0077
  },
}
# Get authentication key from environment variable
SERVICE_AUTH_KEY = os.environ.get("SERVICE_AUTH_KEY")

# Create a Quart app and enable CORS
app = quart_cors.cors(Quart(__name__),
                      allow_origin=[
                        f"http://localhost:{PORT}",
                        "https://chat.openai.com",
                      ])


# Add a route to convert currency
@app.route("/convert", methods=["GET"])
async def convert_currency():
  request_data = await request.get_json()
  from_currency = request_data.get("from_currency")
  to_currency = request_data.get("to_currency")
  amount = float(request_data.get("amount"))

  if from_currency not in CONVERSION_RATES or to_currency not in CONVERSION_RATES[
      from_currency]:
    return jsonify({"error": "Invalid currency pair"}), 400

  converted_amount = amount * CONVERSION_RATES[from_currency][to_currency]
  return jsonify({"converted_amount": converted_amount})


def main():
  app.run(debug=True, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
  main()
