from flask import Flask, request
from flask_restful import Resource, Api
import requests
import json
from classes.router import Router

app = Flask(__name__)
api = Api(app)

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

    def post(self):
        print('Post request received in MainEntry')
        router = Router()
        post_data = request.get_json(force=True)

        try:
            route = router.get_model_route(post_data['model_id'])
        except KeyError as ex:
            return ex

        r = requests.post(route, data=json.dumps(post_data['data']), headers={'Content-Type': 'application/json'})
        return r.json()


class TestRunning(Resource):
    def get(self):
        return 'MainEntry up and running...'

api.add_resource(MainEntry, '/')
api.add_resource(TestRunning, '/test')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
