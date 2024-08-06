import React, { useContext } from 'react';
import { Context } from './Context';
import { useNavigate } from 'react-router-dom';

function Logout() {

    const { setTraveler } = useContext(Context);

    const navigate = useNavigate();

    function handleLogoutClick() {
        console.log("Logout button clicked")
        fetch("/logout", { method: "DELETE" }).then((r) => {
            if (r.ok) {
                setTraveler(null)
            }
        })
        navigate('/login')
    }

    return(
        <div>
            <button onClick={() => handleLogoutClick()}>Logout</button>
        </div>
    )
}

export default Logout;