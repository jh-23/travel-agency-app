import { useState, createContext } from 'react';
import { useParams } from 'react-router-dom';
const Context = createContext()


function ContextProvider({ children }) {

    const [traveler, setTraveler] = useState(null);
    const [destinations, setDestinations] = useState([]);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [showSignUp, setShowSignUp] = useState(false);
    const [activities, setActivities] = useState([]);
    const [destinationId, setDestinationId] = useState([]);


    return(
        <Context.Provider value ={{ username, setUsername, password, setPassword, errors, setErrors, isLoading, setIsLoading, showSignUp, setShowSignUp, traveler, setTraveler, destinations, setDestinations, activities, setActivities, destinationId, setDestinationId }}>
            {children}
        </Context.Provider>
    )
}

export {ContextProvider, Context}