from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/api/<element>/', methods=['GET'])
def json_datas(element):
    base_url = 'https://my-json-server.typicode.com/depth0/survey1/'

    if element == 'student':
        json_file = f'{base_url}surveys'
    elif element == 'bachelor':
        json_file = f'{base_url}questions'
    else:
        return jsonify({'error': 'Invalid element'})

    try:
        response = requests.get(json_file)
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': f'Request failed with status code {response.status_code}'})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)





