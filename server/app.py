#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
# Add your model imports
from models import Traveler, TravelerDestination, Destination, Activity, Itinerary

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# RESTful Routes

class Travelers(Resource):
    
    def get(self):
        
        traveler_dict_list = [traveler.to_dict(only=['username']) for traveler in Traveler.query.all()]
        
        response = make_response(
            traveler_dict_list,
            200
        )
        
        return response

api.add_resource(Travelers, '/travelers')






if __name__ == '__main__':
    app.run(port=7777, debug=True)

