import { NavLink } from 'react-router-dom';
import "./NavBar.css"

function NavBar() {

    return(
        <div>
            <header>
                <nav>
                    <NavLink
                    to="/"
                    className="nav-link"
                    >
                    Home
                    </NavLink>
                    <NavLink
                    to="/destinations"
                    className="nav-link"
                    >
                    Destinations
                    </NavLink>
                    <NavLink
                    to="/itineraries"
                    className="nav-link"
                    >
                    Itineraries
                    </NavLink>
                    <NavLink
                    to="/calendar"
                    className="nav-link"
                    >
                    Calendar
                    </NavLink>
                    <NavLink
                    to="/logout"
                    className="nav-link">
                    Logout
                    </NavLink>

                </nav>
            </header>
        </div>
    )
}

export default NavBar;