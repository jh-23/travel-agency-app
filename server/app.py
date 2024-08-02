#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session, jsonify
from flask_restful import Resource
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Local imports
from config import app, db, api
# Add your model imports
from models import Traveler, TravelerDestination, Destination, ActivityDestination, AvailableActivity, Activity, Itinerary

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# RESTful Routes

class Travelers(Resource):
    
    def get(self):
        
        traveler_dict_list = [traveler.to_dict(only=('username', 'birth_date')) for traveler in Traveler.query.all()]
        
        response = make_response(
            traveler_dict_list,
            200
        )
        
        return response

api.add_resource(Travelers, '/travelers')

class TravelerDestinations(Resource):
    
    def get(self, id):
        
        response_dict = Traveler.query.filter_by(id=id).first().to_dict(only=('traveler_destinations.destination.city', 'traveler_destinations.destination.state', 'traveler_destinations.destination.country', 'traveler_destinations.destination.image'))
        
        response = make_response(
            response_dict,
            200
        )
        
        return response
    
api.add_resource(TravelerDestinations, '/travelerdestinations/<int:id>')

# single traveler resource

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
    
    def get(self, id):
        
        destination = Destination.query.filter_by(id=id).first()
        
        if not destination:
            return make_response({'error': 'Destination not found'}, 404)
        
        # Collect unique activities using a set comprehension and then convert to a list
        unique_activities = list({activity for activity in destination.available_activities})
        
        response_dict = [activity.to_dict(only=('activity_description', 'activity_name', 'activity_image')) for activity in unique_activities]

        response = make_response(
            response_dict,
            200
        )
        
        return response
    
api.add_resource(ActivityByDestination, '/activitybydestination/<int:id>')

class AddActivityToItinerary(Resource):
    
    def post(self):
        
        json = request.get_json()
        
        start_date = datetime.strptime(json.get('start_date'), '%m/%d/%Y').date()
        end_date = datetime.strptime(json.get('end_date'), '%m/%d/%Y').date()
        
        itinerary_id = json.get('itinerary_id')
        itinerary = db.session.get(Itinerary, itinerary_id)
        
        if not itinerary:
            return {"message": "Itinerary not found"}, 404
        
        added_activity = Activity(
            activity_name = json.get('activity_name'),
            activity_description = json.get('activity_description'),
            activity_image = json.get('activity_image'),
            start_date = start_date,
            end_date = end_date,
            traveler_id = json.get('traveler_id'),
            itinerary_id = json.get('itinerary_id')
        )
        
        # itinerary.activities.append(added_activity)
    
        db.session.add(added_activity)
        db.session.commit()
        
        response_dict = added_activity.to_dict()
        
        response = make_response(
            response_dict,
            201
        )
        
        return response

api.add_resource(AddActivityToItinerary, '/add_activity_to_itinerary')
        
class TravelerActivititesToItineraryGet(Resource):
    
    def get(self, itinerary_id):     
        
        itinerary = db.session.get(Itinerary, itinerary_id)
        if not itinerary:
            return {"message": "Itinerary not found"}, 404
        
        response_dict = itinerary.to_dict()
        return make_response(
            response_dict,
            200
        )
        
api.add_resource(TravelerActivititesToItineraryGet, '/get_traveler_itinerary/<int:itinerary_id>')

class DeleteActivityFromItinerary(Resource):
    
    def delete(self, id):
        
        activity = Activity.query.filter_by(id=id).first()
        
        if not activity:
            return {'message': 'Activity not found or does not belong to the specificed traveler and itinerary'}, 404
        
        db.session.delete(activity)
        db.session.commit()
    
        response = make_response(
            {'message': 'successful deletion of activity from itinerary'},
            202
        )
        
        return response
    
api.add_resource(DeleteActivityFromItinerary, '/delete_activity/<int:id>')

class UpdateActivityFromItinerary(Resource):
    
    def patch(self, id):
        
        json = request.get_json()
        
        activity = Activity.query.filter(Activity.id == id).first()
        if not activity:
            return {'message': 'Activity not found'}, 404
        
        if 'start_date' in json:
            start_date = datetime.strptime(json.get('start_date'), '%m/%d/%Y').date()
            activity.start_date = start_date
        
        if 'end_date' in json:
            end_date = datetime.strptime(json.get('end_date'), '%m/%d/%Y').date()
            activity.end_date = end_date
        
        for attr, value in json.items():
            if attr not in ['start_date', 'end_date']:
                setattr(activity, attr, value)
        
        db.session.add(activity)
        db.session.commit()
        
        response = make_response(
            activity.to_dict(),
            200
        )
        
        return response 
    
api.add_resource(UpdateActivityFromItinerary, '/updated_activity_on_itinerary/<int:id>')
            
        
        
# class TravelerItinerary(Resource):
    
#     def get(self, id):
        
#         response_dict = Traveler.query.filter_by(id=id).first().to_dict(only=('activities.itinerary.name',))
        
#         response = make_response(
#             response_dict,
#             200
#         )
        
#         return response 
    
# api.add_resource(TravelerItinerary, '/itinerary/<int:id>')


class TravelerItinerary(Resource):
    
    def get(self, id):
        
        traveler = Traveler.query.filter_by(id=id).first()
        
        if not traveler:
            return make_response({'error': 'Traveler not found'}, 404)
        
        # Collect unique itineraries using a set comprehension and then convert to a list
        unique_itineraries = list({activity.itinerary.name for activity in traveler.activities if activity.itinerary})
        
        response = make_response({'itineraries': unique_itineraries}, 200)
        
        return response 
    
api.add_resource(TravelerItinerary, '/itinerary/<int:id>')









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


# class ActivityByDestination(Resource):

#     def get(self, id):
    
#         response_dict = Destination.query.filter_by(id=id).first().to_dict(only=('activity_destinations.activity.activity_description', 'activity_destinations.activity.activity_image', 'activity_destinations.activity.activity_name'))
        
#         response = make_response(
#             response_dict,
#             200
#         )
        
#         return response 
    
# api.add_resource(ActivityByDestination, '/activitybydestination/<int:id>')

if __name__ == '__main__':
    app.run(port=7777, debug=True)

