import os

from flask import Flask

app = Flask(__name__)

#@app.route("/")
@app.route('/getContent/<role>')
def get_content(role):
    if role == 'teacher':
        return "You are the teacher direct your pupils!"
    elif role == 'pupil':
        return "You are a pupil get directed your teacher!"
    else:
        return "Invalid role"












if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
  app.run(debug=True, host='0.0.0.0', port=port)
