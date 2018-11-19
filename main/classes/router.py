core_dict = {
    'py_model_1': {
        'id': 'py_model_1',
        'lang': 'python',
        'container_name': 'py_model_1',
        'route': 'http://py_model_1:8000',
        'dev_route': 'http://127.0.0.2:8000'
    },
    'r_model_1': {
        'id': 'r_model_1',
        'lang': 'R',
        'container_name': 'r_model_1',
        'route': 'http://r_model_1:8000',
        'dev_route': 'http://127.0.0.3:8000'
    }
}
import json

class Router():
    def __init__(self, data=core_dict):
        self.__dict__ = data

    def get_model(self, id):
        if id in self.__dict__:
            return self.__dict__[id]
        else:
            raise KeyError('No model found with id: ' + id)

    def get_model_route(self, id):
        if id in self.__dict__:
            return self.__dict__[id]['route']
        else:
            raise KeyError('No model found with id: ' + id)
