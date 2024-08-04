import React, { useState, useEffect} from 'react';
import { useParams } from 'react-router-dom'

function Destinations() {

    const [destinations, setDestinations] = useState([]);

    useEffect(() => {
        fetch(`/travelerdestinations`)
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
                console.error('Error fetching podcasts: ', error)
            })
    }, [setDestinations])

    if(!destinations) {
        return <h1>Loading...</h1>
    }

    console.log(destinations);

    return(
        <div>
            <h1>Destinations</h1>
        </div>
    )
}

export default Destinations;