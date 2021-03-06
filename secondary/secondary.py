from flask import Flask, request
from flask_restful import Resource, Api
import Model

app = Flask(__name__)
api = Api(app)

class SecondaryEntry(Resource):
    def get(self):
        return 'SecondaryEntry is running sucessfully'

    def post(self):
        print('Get request received in SecondaryEntry')
        data = request.get_json()
        print(data)
        return {
            'model_id': 'py_model_1',
            'score': 0.59736
        }

api.add_resource(SecondaryEntry, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
