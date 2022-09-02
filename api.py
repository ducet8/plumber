import json
import os
import subprocess

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Status(Resource):
    def get(self):
        return {"container status": "200"}, 200

    def post(self):
        return {"container status": "200"}, 200


class Action(Resource):
    def post(self):
        # TODO: Post code for storing action file
        pass


class Flushed(Resource):
    def post(self, sku):
        print({'triggered': sku})
        payload = request.get_json(force=True)
        # TODO: Call code in entry


class Pipe(Resource):
    def get(self, sku):
        return {'content': json.loads(subprocess.check_output(f'cat {os.getcwd()}/configuration/pipes/{sku}.json', shell=True))}

    def put(self, sku):
        # TODO: Put code for updating a pipe
        pass


class Pipes(Resource):
    def get(self):
        pipes = []
        for file in os.listdir(f'{os.getcwd()}/configuration/pipes/'):
            if file.endswith('.yml') or file.endswith('.json'):
                pipes.append(file.split('.')[0])
        return {'pipes': pipes}

    def post(self):
        # TODO: Post code for storing as a pipe
        pass


class Trigger(Resource):
    def post(self):
        # TODO: Post code for storing trigger file
        pass


api.add_resource(Status, '/')
api.add_resource(Pipes, '/action')
api.add_resource(Flushed, '/flushed/<sku>')
api.add_resource(Pipe, '/pipe/<sku>')
api.add_resource(Pipes, '/pipes')
api.add_resource(Pipes, '/trigger')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
