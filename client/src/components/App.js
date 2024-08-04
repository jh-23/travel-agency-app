import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./NavBar";
import LoginForm from "./LoginForm";

function App() {

  const [traveler, setTraveler] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((traveler) => setTraveler(traveler))
      }
    })
  }, [])

  if(!traveler) return <LoginForm setTraveler={setTraveler} />

  console.log(traveler)



  return(
    <div className="App">
        <header>
        <NavBar />
        </header>
        <h1 className='text-6xl'>Travel Agency App</h1>
    </div>
  )
}

export default App;
