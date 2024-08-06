import React, { useState, useEffect, useContext} from 'react';
import { Context } from './Context';

function Destinations() {

    const { destinations, setDestinations } = useContext(Context);


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

    console.log(destinations[0].city);
    const cities = destinations.map((destination) => destination.city)
    console.log(cities)

    return(
        <div>
            <h1>Destinations</h1>
        </div>
    )
}

export default Destinations;