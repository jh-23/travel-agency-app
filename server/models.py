from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates 
from sqlalchemy.ext.hybrid import hybrid_property


from config import db, bcrypt

# Models go here

class Traveler(db.Model, SerializerMixin):
    
    __tablename__ = 'travelers'
    
    serialize_rules = ('-traveler_destinations.traveler', '-traveler_destinations', '-activities.traveler', '-activities',)
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    _password_hash = db.Column(db.String(50))
    birth_date = db.Column(db.String)
    
    
    traveler_destinations = db.relationship('TravelerDestination', back_populates='traveler', cascade='all, delete-orphan')
    
    activities = db.Relationship('Activity', back_populates='traveler', cascade='all, delete-orphan')
    
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
    
    serialize_rules = ('-traveler_destinations.destination',)
    
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String)
    country = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    
    # Relationship mapping the destination to related traveler
    traveler_destinations = db.relationship('TravelerDestination', back_populates='destination')
    
class Activity(db.Model, SerializerMixin):
    
    __tablename__ = 'activities'
    
    serialize_rules = ('-traveler.activities', '-itinerary.activities')
    
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String, nullable=False)
    activity_description = db.Column(db.String, nullable=False)
    activity_image = db.Column(db.String, nullable=False)
    
    #Foreign Keys
    traveler_id = db.Column(db.Integer, db.ForeignKey('travelers.id'))
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'))
    
    # Relationship mapping the Activity to related traveler
    traveler = db.relationship('Traveler', back_populates='activities')
    
    # Relationship mapping the Activity to related itinerary
    itinerary = db.relationship('Itinerary', back_populates='activities')
    
    
class Itinerary(db.Model, SerializerMixin):
    
    __tablename__ = 'itineraries'
    
    serialize_rules = ('-activities.itinerary', )
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    
    # Relationship mapping the Itinerary to related Activities 
    
    activities = db.relationship('Activity', back_populates='itinerary', cascade='all, delete-orphan')
    