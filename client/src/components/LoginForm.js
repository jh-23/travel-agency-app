import React, { useState } from 'react';
import Input from './Input';

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
            <h1>Welcome to the Travel Agency App</h1>
            <h4>Please sign in to view travel information: </h4>
            <br />
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor='username'>Username: </label>
                    <Input
                    type='text'
                    id='username'
                    autoComplete='off'
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}>
                </Input>
                </div>
                <br />
                <div>
                    <label htmlFor='password'>Password: </label>
                    <Input
                    type='password'
                    id='password'
                    autoComplete='current-password'
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}>
                    </Input>
                </div>
                <button type='submit' className="btn btn-blue">
                    {isLoading ? "Loading..." : "Login"}
                </button>
            </form>
            {errors.length > 0 && (
                <div>
                    {errors.map((error, index) => (
                        <p key={index} style={{ color: 'red' }}>{error}</p>
                    ))}
                </div>
            )}
        </div>
    )
}

export default LoginForm;