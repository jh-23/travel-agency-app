#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
from datetime import datetime

# Remote library imports
# from faker import Faker

# Local imports
from app import app
from config import db 
from models import Traveler, TravelerDestination, Destination, ActivityDestination, Activity, Itinerary, AvailableActivity

# if __name__ == '__main__':
#     fake = Faker()
with app.app_context():
        # db.create_all()
        print("Starting seed...")
        # Seed code goes here!
        
        Traveler.query.delete()
        TravelerDestination.query.delete()
        Destination.query.delete()
        AvailableActivity.query.delete()
        Activity.query.delete()
        Itinerary.query.delete()
        
        # Seed travelers database 
        
        travelers_to_add = []
        
        traveler1 = (Traveler(
            id=1,
            username="billyjane",
            birth_date=datetime(1980, 3, 25),
            email = "billyjane@gmail.com"
        ))
        traveler1.password_hash = "welttraveler8"
        
        traveler2 = (Traveler(
            id=2,
            username="sarahjane",
            birth_date=datetime(1985, 11, 1),
            email = "sarahjane@gmail.com"
        ))
        traveler2.password_hash = "9899trail0"
        
        travelers_to_add.append(traveler1)
        travelers_to_add.append(traveler2)
        db.session.add_all(travelers_to_add)
        
        
        # Seed traveler_destination table
        traveler_destinations_to_add = []
        
        traveler_destination1 = (TravelerDestination(
            traveler_id=1,
            destination_id=1
        ))
        
        traveler_destination2 = (TravelerDestination(
            traveler_id=2,
            destination_id=2
        ))
        
        traveler_destinations_to_add.append(traveler_destination1)
        traveler_destinations_to_add.append(traveler_destination2)
        db.session.add_all(traveler_destinations_to_add)
        
        # Seed Destinations to database
        destinations_to_add = []
        
        destination1 = (Destination(
            id=1,
            city= "New York City",
            state= "NY",
            country= "USA",
            image="https://i.natgeofe.com/n/874df281-d3e0-489a-98c0-6b840023b828/newyork_NationalGeographic_2328428.jpg?w=2048&h=1366"
        ))
        
        destination2 = (Destination(
            id=2,
            city="Zurich",
            state="N/A",
            country="Switzerland",
            image="https://i.natgeofe.com/n/ba9f1ab4-3abe-4b95-a884-90fc45d17db3/city-aerial-zurich-switzerland.jpg?w=2880&h=2158"
        ))
        
        destinations_to_add.append(destination1)
        destinations_to_add.append(destination2)
        db.session.add_all(destinations_to_add)
        
        # Seed ActivityDestination to Database
        activity_destinations_to_add = []
        
        activity_destination_1 = (ActivityDestination(
            destination_id=1,
            activity_id=1
        ))
        
        activity_destination_2 = (ActivityDestination(
            destination_id=1,
            activity_id=2
        ))
        
        activity_destination_3 = (ActivityDestination(
            destination_id=2,
            activity_id=3
        ))
        
        activity_destination_4 = (ActivityDestination(
            destination_id=2,
            activity_id=4
        ))
        
        activity_destinations_to_add.append(activity_destination_1)
        activity_destinations_to_add.append(activity_destination_2)
        activity_destinations_to_add.append(activity_destination_3)
        activity_destinations_to_add.append(activity_destination_4)
        db.session.add_all(activity_destinations_to_add)
        
        # Seed Activity Column
        
        activities_to_add = []
        
        activity_1 = (AvailableActivity(
            id=1,
            activity_name = "Ellis Island",
            activity_description = "Ellis Island is a federally owned island in New York Harbor, situated within the U.S. states of New Jersey and New York. Ellis Island was once the busiest immigrant inspection and processing station in the United States. From 1892 to 1954, nearly 12 million immigrants arriving at the Port of New York and New Jersey were processed there.[6] It has been part of the Statue of Liberty National Monument since 1965 and is accessible to the public only by ferry. The north side of the island is a national museum of immigration, while the south side of the island, including the Ellis Island Immigrant Hospital, is open to the public through guided tours.",
            activity_image = "https://www.statueofliberty.org/wp-content/uploads/2020/08/APS_5690-scaled.jpg",
            start_date = datetime(2025, 7, 3),
            end_date = datetime(2025, 7, 3),
            destination_id = 1
        ))
        
        activity_2 = (AvailableActivity(
            id=2,
            activity_name="The Metropolitan Museum of Art",
            activity_description = "The Metropolitan Museum of Art presents over 5,000 years of art from around the world for everyone to experience and enjoy. The Museum lives in two iconic sites in New York City—The Met Fifth Avenue and The Met Cloisters. Millions of people also take part in The Met experience online.  Since its founding in 1870, The Met has always aspired to be more than a treasury of rare and beautiful objects. Every day, art comes alive in the Museum's galleries and through its exhibitions and events, revealing new ideas and unexpected connections across time and across cultures.",
            activity_image = "https://cdn.sanity.io/images/cctd4ker/production/909fa245367580e643fff7bedf1f5ca129443163-1200x630.jpg?w=600&q=75&auto=format",
            start_date= datetime(2025, 7, 5),
            end_date = datetime(2025, 7, 5),
            destination_id = 1
        ))
    
        activity_3 = (AvailableActivity(
            id=3,
            activity_name="Old Town",
            activity_description="Also known as Alstadt, Zurich's historical center is a cool mix of old and new. It's home to iconic churches like the twin towers of Grossmunster as well as Fraumunster, which is famous for its stained glass windows. You can also climb up Lindenhof Hill for a bird's eye view of the town and walk the pedestrianized streets of Niederdorf and Limmatquai—they are lively with shops by day and packed with nightlife as the sun goes down. Join a walking tour to explore the medieval alleyways or hop on a cruise along River Limmat for a different view of the picturesque Old Town. ",
            activity_image="https://travel.usnews.com/images/Zurich_Sunrise.jpg",
            start_date = datetime(2025, 8, 3),
            end_date = datetime(2025, 8, 4),
            destination_id = 2
        ))
        
        activity_4 = (AvailableActivity(
            id=4,
            activity_name="Uetliberg",
            activity_description="Standing an impressive 2,858 feet above sea level, Uetliberg offers some of the best views of Zurich and the surrounding alps. Once at the top, travelers will find multiple trails through the dense and ancient yew tree groves for hiking, extreme mountain biking and sledding. Paragliding at the mountain's peak is another popular pastime here.",
            activity_image="https://travel.usnews.com/dims4/USNEWS/7f74556/2147483647/resize/976x652%5E%3E/crop/976x652/quality/85/?url=https%3A%2F%2Ftravel.usnews.com%2Fimages%2FUetliberg_Mountain_Stanley_Chen_Xi_Getty.jpg",
            start_date = datetime(2025, 8, 4),
            end_date = datetime(2025, 8, 4),
            destination_id = 2
        ))
    
        activities_to_add.append(activity_1)
        activities_to_add.append(activity_2)
        activities_to_add.append(activity_3)
        activities_to_add.append(activity_4)
        db.session.add_all(activities_to_add)

    
        # Seed Itinerary Column
        
        itineraries_to_add = []
        
        itinerary_1 = (Itinerary(
            id=1,
            name="New York Trip"
        ))
        
        itinerary_2 = (Itinerary(
            id=2,
            name="Zurich Trip"
        ))
        
    
        itineraries_to_add.append(itinerary_1)
        itineraries_to_add.append(itinerary_2)
        db.session.add_all(itineraries_to_add)
        
        db.session.commit()
        
        
        