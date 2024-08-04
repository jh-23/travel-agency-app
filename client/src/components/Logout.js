import React, { useContext } from 'react';
import { Context } from './Context';

function Logout() {

    const { setTraveler } = useContext(Context);

    function handleLogoutClick() {
        console.log("hello")
        fetch("/logout", { method: "DELETE" }).then((r) => {
            
            if (r.ok) {
                setTraveler(null)
            }
        })
    }



    return(
        <div>
            <button id='test' onClick={() => handleLogoutClick()}></button>
        </div>
    )
}

export default Logout;