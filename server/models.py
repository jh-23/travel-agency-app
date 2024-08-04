from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates 
from sqlalchemy.ext.hybrid import hybrid_property


from config import db, bcrypt


# Models go here

class Traveler(db.Model, SerializerMixin):
    
    __tablename__ = 'travelers'
    
    # serialize_rules = ('-traveler_destinations.traveler.traveler_destinations', '-activities.traveler', '-activities.destinations', '-activities.activity_destinations', '-traveler_destinations.destination.traveler_destinations', '-activities.destination.traveler_destinations', '-activities.destination.activity_destinations', '-travel_destinations.destination.activity_destinations', '-traveler_destinations.destination.activities')
    serialize_rules = ('-traveler_destinations.traveler', '-activities', '-destinations.traveler_destinations', '-itineraries.activities')
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.String(db.String(50))
    username = db.Column(db.String(50))
    _password_hash = db.Column(db.String(128), nullable=False)
    birth_date = db.Column(db.String)
    
    traveler_destinations = db.relationship('TravelerDestination', back_populates='traveler', cascade='all, delete-orphan')
    
    activities = db.relationship('Activity', back_populates='traveler', cascade='all, delete-orphan')
    
    # Association Proxy
    destinations = association_proxy('traveler_destinations', 'destination', creator=lambda destination_obj: TravelerDestination(destination=destination_obj))
    
    # Association Proxy
    itineraries = association_proxy('activities', 'itinerary', creator=lambda itinerary_obj: Activity(itinerary=itinerary_obj))
    
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
        
    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8')
        )
    
    
class TravelerDestination(db.Model, SerializerMixin):
    
    __tablename__ = 'traveler_destinations'
    
    serialize_rules = ('-traveler.traveler_destinations', '-destination.traveler_destinations')
    
    id = db.Column(db.Integer, primary_key=True)
    
    #Foreign Keys
    traveler_id = db.Column(db.Integer, db.ForeignKey('travelers.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
    
    # relationship method maps our TravelerDestination to Traveler
    traveler = db.relationship('Traveler', back_populates='traveler_destinations')
    
    # relationship method maps our TravelerDestination to Destination
    destination = db.relationship('Destination', back_populates='traveler_destinations')
    
class Destination(db.Model, SerializerMixin):
    
    __tablename__ = 'destinations'
    
    serialize_rules = ('-traveler_destinations.destination', '-activity_destinations.destination', '-activities.destinations', '-available_activities.destination')
    
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String)
    country = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    
    # Relationship mapping the destination to related traveler
    traveler_destinations = db.relationship('TravelerDestination', back_populates='destination')
    
    # Relationship mapping the Destination to related Activity 
    activity_destinations = db.relationship('ActivityDestination', back_populates='destination', cascade='all, delete-orphan')
    
    available_activities = db.relationship('AvailableActivity', back_populates='destination')
    
    # Need to build association relationship -> #association_proxy = to associate activities with the Destination (condense information into a clearer list)
    # Association proxy to get Actvities for this destination through ActivityDestination
    activities = association_proxy('activity_destinations', 'activity', creator=lambda activity_obj: ActivityDestination(activity=activity_obj))
    
    
class ActivityDestination(db.Model, SerializerMixin):
    
    __tablename__ = 'activity_destinations'
    
    serialize_rules = ('-destination.activity_destinations', '-activity.activity_destinations')
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys
    
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    
    
    # db.relationships as well
    
    destination = db.relationship('Destination', back_populates='activity_destinations')
    
    activity = db.relationship('Activity', back_populates='activity_destinations')
    
    
class Activity(db.Model, SerializerMixin):
    
    __tablename__ = 'activities'
    
    serialize_rules = ('-traveler.activities', '-itinerary.activities', '-activity_destinations.activity', '-destinations.activity_destinations', '-destinations.activities')
    
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String, nullable=False)
    activity_description = db.Column(db.String, nullable=False)
    activity_image = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    
    #Foreign Keys
    traveler_id = db.Column(db.Integer, db.ForeignKey('travelers.id'))
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'))

    # Relationship mapping the Activity to related traveler
    traveler = db.relationship('Traveler', back_populates='activities')
    
    # Relationship mapping the Activity to related itinerary
    itinerary = db.relationship('Itinerary', back_populates='activities')
    
    # Relationship Mapping the Activity to related destination
    activity_destinations = db.relationship('ActivityDestination', back_populates='activity', cascade='all, delete-orphan')
    
    # Association proxy to get destinations for this activity through ActivityDestination
    destinations = association_proxy('activity_destinations', 'destination', creator=lambda destination_obj: ActivityDestination(destination=destination_obj))
    
    def to_dict(self):
        return {
            'id': self.id,
            'activity_name': self.activity_name,
            'activity_description': self.activity_description,
            'activity_image': self.activity_image,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'traveler_id': self.traveler_id,
            'itinerary_id': self.itinerary_id
        }
        
class AvailableActivity(db.Model, SerializerMixin):
    
    __tablename__ = 'available_activities'
    
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String, nullable=False)
    activity_description = db.Column(db.String, nullable=False)
    activity_image = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    
    # foreign key
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
    
    # Relationship mapping the Available Actities to related destination
    destination = db.relationship('Destination', back_populates='available_activities')
    
    
class Itinerary(db.Model, SerializerMixin):
    
    __tablename__ = 'itineraries'
    
    serialize_rules = ('-activities.itinerary', )
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


    # Relationship mapping the Itinerary to related Activities 
    
    activities = db.relationship('Activity', back_populates='itinerary', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'activities': [activity.to_dict() for activity in self.activities]
        }