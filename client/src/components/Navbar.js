import { NavLink } from 'react-router-dom';

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
                    to="">

                    </NavLink>

                </nav>
            </header>
        </div>
    )
}

export default NavBar;