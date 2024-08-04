import React, { useContext } from 'react';
import { Context } from './Context';

function Logout() {

    const { setTraveler } = useContext(Context);

    function handleLogoutClick() {
        fetch("/logout", { method: "DELETE" }).then((r) => {
            if (r.ok) {
                setTraveler(null)
            }
        })
    }

    return(
        <div>
            <button onClick={handleLogoutClick}></button>
        </div>
    )
}

export default Logout;