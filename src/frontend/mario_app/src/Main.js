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
import './Main.css';
import BattingStatsTable from './Table/BattingStatsTable';
import StandingsTable from './Table/StandingsTable';

import teamLogo from "./Images/Teams/Luigi Knights logo.png"
import mzoneLogo from "./Images/lVl Logo.png"
import superSluggersLogo from "./Images/Mario Super Sluggers Logo.png"

function Main() {
    console.log(teamLogo);
    return (
        <div class="body">
            <nav class="navbar background">
                <div class="nav-list">
                    <div class="logo">
                        <img src={teamLogo} alt="Team Logo"/>
                    </div>
                    <li><a>Luigi Knights</a></li>
                </div>
            </nav>
            <div class="container">
                    <div class="firstHalf">
                        <button class="text-big">
                            Play Game @ Bowser
                        </button>
                        <p class="text-small">
                            Last Game: <br/>
                            &nbsp; Mario 6 <br/>
                            &nbsp; Luigi 7 &gt;
                        </p>
                        <div class="previous">
                            <button>Previous Seasons</button>
                        </div>
                        <div class="info">
                            <div class="year">2016</div>
                            <div class="version">v1.4</div>
                        </div>
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
                        <BattingStatsTable/>
                        <div class="standings">
                            <div class="division division-border division-border-right">
                                <StandingsTable/>
                            </div>
                            <div class="division division-border">
                                <StandingsTable/>
                            </div>
                        </div>
                    </div>
            </div>
            <nav class="navbar background">
                <ul class="nav-list">
                    <div class="bottomLogo">
                        <img src={mzoneLogo} alt="mzone"/>
                    </div>
                    <div class="bottomLogo bottomRight">
                        <img src={superSluggersLogo} alt="Mario Super Sluggers"/>
                    </div>
                </ul>
            </nav>
        </div>
    )
}
  
export default Main