from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder="../dist", static_folder="../dist/static")

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def test_api():
  data = {'name': 'maleic',
          'message': 'Hello, vue and flask!'}
  return jsonify(data)