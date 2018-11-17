from flask import Flask
from flask_restful import Resource, Api
import requests
import json

app = Flask(__name__)
api = Api(app)
address = 'http://secondary'
#address = 'http://0.0.0.0:801/'

class MainEntry(Resource):
    def get(self):
        print('Get request received in MainEntry')
        data = {
            'id': 1,
            'input': {
                'main': 'foo',
                'secondary': 'bar'
            }
        }
        print(data)
        r = requests.post(address, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        return r.json()

class TestRunning(Resource):
    def get(self):
        return 'MainEntry up and running...'

api.add_resource(MainEntry, '/')
api.add_resource(TestRunning, '/test')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
