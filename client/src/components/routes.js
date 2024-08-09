import App from './App.js'
import Home from './Home.js'
import Destinations from './Destinations.js';
import Itinerary from './Itinerary.js';
import Calendar from './Calendar.js';
import Logout from './Logout.js';
import LoginForm from './LoginForm.js';
import Activities from './Activities.js';


const routes = [
    {
        path:"/",
        element: <App />,
    },
    {
        path: "/home",
        element: <Home />
    },
    {
        path: "/login",
        element: <LoginForm />
    },
    {
        path: "/destinations",
        element: <Destinations />
    },
    {
        path:"/activities",
        element: <Activities />
    },
    {
        path: "/itineraries",
        element: <Itinerary />
    },
    {
        path: "/calendar",
        element: <Calendar />
    }, 
    {
        path: "/logout",
        element: <Logout />
    }

]

export default routes;