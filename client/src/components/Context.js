import { useState, createContext } from 'react';
const Context = createContext()

function ContextProvider({ children }) {

    const [traveler, setTraveler] = useState([]);
    const [destinations, setDestinations] = useState([]);

    return(
        <Context.Provider value ={{traveler, setTraveler, destinations, setDestinations}}>
            {children}
        </Context.Provider>
    )
}

export {ContextProvider, Context}