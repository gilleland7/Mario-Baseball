// Importing modules
//import React, { useState, useEffect } from "react";
//import "./App.css";
 
/*function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        name: "",
        age: 0,
        ex: "",
        programming: "",
    });
 
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
        fetch("/data").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    name: data.Name,
                    age: data.Age,
                    ex: data.ex,
                    programming: data.programming,
                });
            })
        );
    }, []);
 
    return (
        <div className="App">
            <header className="App-header">
                <h1>React and flask</h1>
                {/* Calling a data from setdata for showing }
                <p>{data.name}</p>
                <p>{data.age}</p>
                <p>{data.ex}</p>
                <p>"HERE"</p>
                <p>{data.programming}</p>
 
            </header>
        </div>
    );
}
 
export default App;

*/

import React from 'react';
import './App.css';

function App() {
    return (
        <div class="body">
            <nav class="navbar background">
                <ul class="nav-list">
                    <div class="logo">
                        <img src=
"https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210420155809/gfg-new-logo.png" />
                    </div>
                    <li><a>Luigi Knights</a></li>
                </ul>
            </nav>
            <section class="container">
                    <div class="firstHalf">
                        <button class="text-big">
                            Play Game @ Bowser
                        </button>
                        <p class="text-small">
                            Last Game: <br/>
                            &nbsp; Mario 6 <br/>
                            &nbsp; Luigi 7
                        </p>
                    </div>
                    <div class="secondHalf">
                        <div class="stats-container">
                            <div class = "team">
                                <button class="text-big">
                                    &lt; Luigi Knights &gt;
                                </button>
                            </div>
                            <div class = "stats">
                                <button class="text-big">
                                    &lt; Batting Stats &gt;
                                </button>
                            </div>
                        </div>
                        <p class="text-small">
                            JavaScript is the world most popular 
                            lightweight, interpreted compiled 
                            programming language. It is also 
                            known as scripting  language for
                            web pages. It is well-known for 
                            the development of web page many 
                            non-browser environments also use
                            it. JavaScript can be used for 
                            Client-side developments as well 
                            as Server-side developments.
                        </p>
                    </div>
            </section>
            <footer className="footer">
                <p className="text-footer">
                    Copyright ©-All rights are reserved
                </p>
            </footer>
        </div>
    )
}
  
export default App