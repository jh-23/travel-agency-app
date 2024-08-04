import React, { useState } from 'react';

function LoginForm({ setTraveler }) {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [showSignUp, setShowSignUp] = useState(false);

    function handleSubmit(e) {
        e.preventDefault();
        setIsLoading(true);
        fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        }).then((r) => {
            setIsLoading(false);
            if (r.ok) {
                r.json().then((traveler) => setTraveler(traveler))
            } else {
                r.json().then((err) => setErrors(err.errors))
            }
        })
    }


    return(
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor='username'>Username</label>
                <input
                type='text'
                id='username'
                autoComplete='off'
                value={username}
                onChange={(e) => setUsername(e.target.value)}>
                </input>
                <br />
                <label htmlFor='password'>Password</label>
                <input
                type='text'
                id='username'
                autoComplete='current-password'
                value={password}
                onChange={(e) => setPassword(e.target.value)}>
                </input>
                <button variant='fill' color='primary' type='submit'>
                    {isLoading ? "Loading..." : "Login"}
                </button>
            </form>
        </div>
    )
}

export default LoginForm;