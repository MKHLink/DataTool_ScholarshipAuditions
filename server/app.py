from flask import Flask, request
from flask_restful import Api,Resource
from connection import client
from routes import ProfessorResource
from routes import ProfessorCreateResource
from routes import ProfessorDeleteResource

from connection import professors_collection
from model import Professor

app = Flask(__name__)
api = Api(app)

api.add_resource(ProfessorResource, '/professors/<string:professor_id>')
api.add_resource(ProfessorCreateResource, '/professor/create')
api.add_resource(ProfessorDeleteResource, '/professor/delete/<string:professor_id>')


if __name__ == '__main__':
    app.run(debug=True)