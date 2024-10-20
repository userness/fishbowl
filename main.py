import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "hi"

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(debug=true, host='0.0.0.0', port=port)