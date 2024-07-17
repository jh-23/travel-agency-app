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

class AllDestinations(Resource):
    
    def get(self):
        
        destination_dict_list = [destination.to_dict(only=('city', 'state', 'country', 'image')) for destination in Destination.query.all()]
        
        response = make_response(
            destination_dict_list,
            200
        )
        
        return response
    
api.add_resource(AllDestinations, '/alldestinations')

class ActivityByDestination(Resource):

    pass








class Login(Resource):
    
    def post(self):
        
        username = request.get_json()['username']
        traveler = Traveler.query.filter(Traveler.username == username).first()
        
        password = request.get_json()['password']
        
        if traveler:
            
            if traveler.authenticate(password):
                session['traveler_id'] = traveler.id
            return traveler.to_dict()
        
        else:
            return {'error': 'Invalid username or password'}, 401
        
api.add_resource(Login, '/login')

class Logout(Resource):
    
    def delete(self):
        
        if session['traveler_id'] != None:
            session['traveler_id'] = None
            return {}, 204
        elif session['traveler_id'] == None:
            return {'error': 'logout was unsuccessful'}
        
api.add_resource(Logout, '/logout', endpoint='logout')

class CheckSession(Resource):
    
    def get(self):
        
        if 'traveler_id' in session:
            traveler_id = session['traveler_id']
            traveler = Traveler.query.filter(Traveler.id == traveler_id).first()
        
            if traveler:
                response = make_response(
                    traveler.to_dict(),
                    200
                    )
            else:
                response = make_response(
                    {'error': 'Traveler not found'},
                    404
                )
        
        else:
            response = make_response(
                {'error': 'No traveler_id in session'},
                401
            )
            
        return response
    
api.add_resource(CheckSession, '/check_session', endpoint='check_session')

class Signup(Resource):
    
    def post(self):
        
        json = request.get_json()
        traveler = Traveler(
            username = json.get('username'),
            birth_date = json.get('birth_date')
        )
        traveler.password_hash = json['password']
        
        try:
            
            db.session.add(traveler)
            db.session.commit()
            session['traveler_id'] = traveler.id
            return traveler.to_dict(), 201
        
        except IntegrityError:
            return {'error': 'Invalid login credentials'}, 401
        
api.add_resource(Signup, '/signup', endpoint='signup')

if __name__ == '__main__':
    app.run(port=7777, debug=True)

