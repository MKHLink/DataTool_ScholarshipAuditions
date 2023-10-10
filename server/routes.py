from flask import request
from flask_restful import Resource
from connection import professors_collection
from model import Professor
from bson import ObjectId

class ProfessorResource(Resource):
    def get(self, professor_id):
        if professor_id == "all":
            # Retrieve all professors from MongoDB
            professors = list(professors_collection.find({}))
            return professors, 200
        else:
            # Retrieve a professor by ID from MongoDB
            professor = professors_collection.find_one({'_id': ObjectId(professor_id)})
            if professor:
                return professor, 200
            return {'message': 'Professor not found'}, 404
    
    def get(self, professor_id):
        # Retrieve a professor by ID from MongoDB
        professor = professors_collection.find_one({'_id': ObjectId(professor_id)})
        if professor:
            return professor, 200
        return {'message': 'Professor not found'}, 404

class ProfessorCreateResource(Resource):
    def post(self):
        # Create a new professor from the request data
        data = request.get_json()
        professor = Professor(**data)
        
        # Insert the professor document into MongoDB
        result = professors_collection.insert_one(professor.__dict__)
        
        return {'message': 'Professor created', 'id': str(result.inserted_id)}, 201

class ProfessorDeleteResource(Resource):
    def delete(self, professor_id):
        # Delete a professor by ID from MongoDB
        result = professors_collection.delete_one({'_id': ObjectId(professor_id)})
        if result.deleted_count > 0:
            return {'message': 'Professor deleted'}, 204
        return {'message': 'Professor not found'}, 404