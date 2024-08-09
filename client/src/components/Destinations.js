import React, { useEffect, useContext} from 'react';
import { Context } from './Context';
import { useNavigate } from 'react-router-dom';
import DestinationCard from './DestinationCard';


function Destinations() {

    const { destinations, setDestinations, destinationId, setDestinationId } = useContext(Context);

    const navigate = useNavigate();


    useEffect(() => {
        fetch("/alldestinations")
            .then((r) => {
                if(!r.ok) {
                    throw new Error('Network response was not ok');
                }
                return r.json();
            })
            .then((destinations) => {
                if (destinations.error) {
                    throw new Error(destinations.error)
                }
                setDestinations(destinations)
            })
            .catch((error) => {
                console.error('Error fetching destinations: ', error)
            })
    }, [setDestinations])

    if(!destinations) {
        return <h1>Loading...</h1>
    }

    console.log(destinations)
    const cities = destinations.map((destination) => destination)
    console.log(cities)


    return(
        <div>
            <h1>Select Destination where you'd like to travel and view travel activities: </h1>
            <div className='destination-container'>
                {destinations.map((destination) => (
                    <DestinationCard key={destination.id} destination={destination} />
                ))}
            </div>

        </div>
    )
}

export default Destinations;