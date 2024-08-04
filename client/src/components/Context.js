import { useState, createContext } from 'react';
const Context = createContext()

function ContextProvider(props) {

    const [traveler, setTraveler] = useState([]);
    const [destinations, setDestinations] = useState([]);

    return(
        <ContextProvider value ={{traveler, setTraveler, destinations, setDestinations}}>
            {props.children}
        </ContextProvider>
    )
}

export {ContextProvider, Context}