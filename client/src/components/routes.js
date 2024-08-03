import App from './App.js'
import Home from './Home.js'
import Destinations from './Destinations.js';
import Itinerary from './Itinerary.js';
import Calendar from './Calendar.js';
import Logout from './Logout.js';


const routes = [
    {
        path:"/",
        element: <App />,
        children: [
            {
                index: true,
                element: <Home />
            },
            {
                index: "/destinations",
                element: <Destinations />
            },
            {
                index: "/itineraries",
                element: <Itinerary />
            },
            {
                index: "/calendar",
                element: <Calendar />
            }, 
            {
                index: "/logout",
                element: <Logout />
            }
        ]
    }
]

export default routes;