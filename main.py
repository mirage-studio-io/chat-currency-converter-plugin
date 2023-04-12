import os
import quart
import quart_cors
from quart import Quart, jsonify, request
from datetime import date

PORT = 5002
CONVERSION_RATES = {
  "USD": {
    "EUR": 0.92,
    "JPY": 133.75
  },
  "EUR": {
    "USD": 1.09,
    "JPY": 146.11
  },
  "JPY": {
    "USD": 0.0075,
    "EUR": 0.0068
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
  from_currency = request.args.get("from_currency")
  to_currency = request.args.get("to_currency")
  amount = float(request.args.get("amount"))

  if from_currency not in CONVERSION_RATES or to_currency not in CONVERSION_RATES[
      from_currency]:
    return jsonify({"error": "Invalid currency pair"}), 400

  converted_amount = amount * CONVERSION_RATES[from_currency][to_currency]
  return jsonify({"converted_amount": converted_amount, "date": date.today()})


@app.get("/logo.png")
async def plugin_logo():
  filename = 'logo.png'
  return await quart.send_file(filename, mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
  host = request.headers['Host']
  with open("manifest.json") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return quart.Response(text, mimetype="text/json")


@app.get("/openapi.json")
async def openapi_spec_json():
  host = request.headers['Host']
  with open("openapi.json") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return quart.Response(text, mimetype="text/json")


def main():
  app.run(debug=True, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
  main()
