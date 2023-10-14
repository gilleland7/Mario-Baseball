import React, { useState, useEffect } from "react";
import './InSeason.css';
import BattingStatsTable from './Table/BattingStatsTable';
import StandingsTable from './Table/StandingsTable';

function InSeason() {    
    const [data, setdata] = useState({
        teamLogo: ""
    });
    
    const images = require.context('../public/Images/', true);

    const mzoneLogo = images('./lVl Logo.png');
    const superSluggersLogo = images('./Mario Super Sluggers Logo.png');

    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
        fetch("/userteam").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    teamLogo: data.teamLogo
                });               
            })
        );
    }, []);   

    function renderContent() {
        let teamLogo = "";
        if (data.teamLogo != null){
            teamLogo = images("./Teams/Luigi Knights logo.png");
        }
        return(
            <div className="body">
                <nav className="navbar background">
                    <div className="nav-list">
                        <div className="logo">
                            <img src={teamLogo} alt="Team Logo"/>
                        </div>
                    </div>
                </nav>
                <div className="container">
                        <div className="firstHalf">
                            <button className="text-big">
                                Play Game @ Bowser
                            </button>
                            <div className="text-small">
                                Last Game: <br/>
                                <div className = "lastGame">
                                    <div className="topTeam"> 
                                        &nbsp; Mario 6 <br/>
                                    </div>
                                    <div className="bottomTeam">
                                        &nbsp; Luigi 7 &lt;
                                    </div>
                                </div>
                            </div>
                            <div className="previous">
                                <button>Previous Seasons</button>
                            </div>
                            <div className="info">
                                <div className="year">2016</div>
                                <div className="version">v1.4</div>
                            </div>
                        </div>
                        <div className="secondHalf">
                            <div className="stats-container">
                                <div className = "team">
                                    <button className="text-big">
                                        &lt; Luigi Knights &gt;
                                    </button>
                                </div>
                                <div className = "stats">
                                    <button className="text-big">
                                        &lt; Batting Stats &gt;
                                    </button>
                                </div>
                            </div>
                            <BattingStatsTable/>
                            <div className="standingsText"> Standings </div>
                            <div className="standings">
                                <div className="division division-border division-border-right">
                                    <StandingsTable/>
                                </div>
                                <div className="division division-border">
                                    <StandingsTable/>
                                </div>
                            </div>
                        </div>
                </div>
                <nav className="navbar background">
                    <ul className="nav-list">
                        <div className="bottomLogo">
                            <img src={mzoneLogo} alt="mzone"/>
                        </div>
                        <div className="bottomLogo bottomRight">
                            <img src={superSluggersLogo} alt="Mario Super Sluggers"/>
                        </div>
                    </ul>
                </nav>
            </div>
        );
    }
    return ( 
        <div>{renderContent()}</div>
    );
}
  
export default InSeason