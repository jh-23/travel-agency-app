import React, { useEffect, useContext} from 'react';
import { Context } from './Context';

function Activities() {

    const { activities, setActivities, destinationId, setDestinationId } = useContext(Context);

    useEffect(() => {
        fetch(`/activitybydestination/${destinationId}`)
            .then((r) => r.json())
            .then((data) => {
                console.log(data)
                setActivities(data)
                console.log(activities)
            })
            .catch((error) => console.error('Error fetching activities: ', error))
    }, [destinationId])

    if(!activities) {
        return <h1>Loading...</h1>
    }

    console.log(destinationId);

    console.log(activities)


    return(
        <div>
            <h1>Activities for Destination: </h1>
            <ul>
                {activities.map(activity => (
                    <li key={activity.id}>
                        <h2>{activity.activity_name}</h2>
                        <p>{activity.activity_description}</p>
                        <img src={activity.activity_image} alt={activity.activity_name} />
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Activities;

